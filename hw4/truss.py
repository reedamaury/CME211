import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.sparse
import scipy.sparse.linalg
from scipy.sparse import csr_matrix


'''This program takes in two arguments of the directory where the folder containing the truss data is located. 
The folder should consists of the following data pertaining to the airfoil: the joint coordinates, beams and the 
corresponding joints that connect them, as well as support reaction forces and external forces corresponding to 
each joint coordinate. The file with information corresponding to joint coordinate information should be named 
joints.dat and the file with the beam information should be named joints.dat. Any deviations from these file names 
will result in a runtime error. Additionally, if the directory in the command line argument does not exits, the 
program will output a runtime error. The program computes the by beam forces by summing the forces in the in x 
and y directions at each joint and constructing a coefficient matrix corresponding to the equations. The A matrix 
contains the coefficients of beam forces as well as the coefficients of the support reaction forces, while the B 
matrix contains coefficients of the external forces. It is important to note that every two rows corresponds to a 
joint - that is the sum of the forces in the x and y directions for the joint. The linear system of equations is 
solved using the formula Ax=B. If the coefficient matrix A is under- or over-defined the program will return a 
runtime error. If an output directory argument is given, the function will save a plot of the truss geometry to 
the said directory.'''

class Truss:
    def __init__(self, inputdirectory_joint, inputdirectory_beam):
        self.inputdirectory_joint = inputdirectory_joint
        self.inputdirectory_beam = inputdirectory_beam
        self.joint_dict = self.get_joint_dict()
        self.beam_dict = self.get_beam_dict()
        self.joint_keys = self.get_joint_keys()
        self.beam_keys = self.get_beam_keys()
        self.beam_coords = self.get_beam_coords()
        self.beam_coefs = self.get_beam_coefs()
        self.beams_conn2_joints = self.get_beams_conn2_joints()
        self.beam_forces_dict = self.get_beam_forces()

    def get_joint_dict(self):
        """look for file containing joint data
        print error if file not found
        read file containing joint data and assign it to dictionary"""
        self.joint_dict = {}
        if not os.path.exists(self.inputdirectory_joint):
            raise RuntimeError("directory does not exist")
        else:
            with open(self.inputdirectory_joint, 'r') as f:
                next(f)
                flines = f.readlines()
                split_lines = [l.split() for l in flines]
                jointdata = list(map(list, zip(*split_lines)))
            for i in range(len(jointdata[0])):
                xy = [(float(jointdata[1][i])), (float(jointdata[2][i]))]
                force = [(float(jointdata[3][i])), (float(jointdata[4][i]))]
                support = [(float(jointdata[5][i]))]
                self.joint_dict[int(jointdata[0][i])] = [xy, force, support]
        return self.joint_dict

    def get_beam_dict(self):
        """look for file containing beam data
        print error if file not found
        read file containing beam data and assign it to dictionary"""
        self.beam_dict = {}
        if not os.path.exists(self.inputdirectory_beam):
            raise RuntimeError("directory does not exist")
        else:

            with open(self.inputdirectory_beam, 'r') as f:
                next(f)
                flines = f.readlines()
                split_lines = [l.split() for l in flines]
                beamdata = list(map(list, zip(*split_lines)))
            for j in range(len(beamdata[0])):
                val = [(int(beamdata[1][j])), (int(beamdata[2][j]))]
                self.beam_dict[int(beamdata[0][j])] = val
        return self.beam_dict

    def get_joint_keys(self):
        """assigns keys from joint dictionary to
            a list. This is the number of joints"""
        self.joint_keys = []
        joint_dict = self.joint_dict
        for key in joint_dict:
            self.joint_keys.append(key)
        return self.joint_keys

    def get_beam_keys(self):
        """assigns keys from beam dictionary to
        a list. This is the number of beams"""
        self.beam_keys = []
        beam_dict = self.beam_dict
        for key in beam_dict:
            self.beam_keys.append(key)
        return self.beam_keys

    def get_beam_coords(self):
        """assigns coordinates of joints connecting beams"""
        joint_keys = self.joint_keys
        beam_keys = self.beam_keys
        self.beam_coords = {}
        for item in beam_keys:
            self.beam_coords[item] = []
        for i in range(len(joint_keys)):
            for j in range(len(beam_keys)):
                if joint_keys[i] in self.beam_dict[beam_keys[j]]:
                    self.beam_coords[beam_keys[j]].append(self.joint_dict[joint_keys[i]][0])
        return self.beam_coords

    def get_beams_conn2_joints(self):
        """finds all beams that connect to each joint"""
        self.beams_conn2_joints = {}
        for key in self.joint_dict:
            self.beams_conn2_joints[key] = []
        for i in range(len(self.joint_dict)):
            for j in range(len(self.beam_dict)):
                if i + 1 in self.beam_dict[j + 1]:
                    self.beams_conn2_joints[i + 1].append(j + 1)
        return self.beams_conn2_joints

    def get_beam_coefs(self):
        """finds the coefficients of beam forces
            to enter into A matrix later"""
        self.beam_coefs = {}
        for i in range(len(self.beam_keys)):
            x1 = self.beam_coords[self.beam_keys[i]][0][0]
            x2 = self.beam_coords[self.beam_keys[i]][1][0]
            y1 = self.beam_coords[self.beam_keys[i]][0][1]
            y2 = self.beam_coords[self.beam_keys[i]][1][1]
            xdist = abs(x2 - x1)
            ydist = abs(y2 - y1)
            bx = xdist / math.sqrt(xdist ** 2 + ydist ** 2)
            by = ydist / math.sqrt(xdist ** 2 + ydist ** 2)
            self.beam_coefs[self.beam_keys[i]] = [bx, by]
        return self.beam_coefs

    def PlotGeometry(self, outputfile):
        """plots the truss geometry and saves it to the
        output file"""
        for i in range(len(self.beam_keys)):
            x1 = self.beam_coords[self.beam_keys[i]][0][0]
            x2 = self.beam_coords[self.beam_keys[i]][1][0]
            y2 = self.beam_coords[self.beam_keys[i]][0][1]
            y1 = self.beam_coords[self.beam_keys[i]][1][1]
            plt.plot([x2, x1], [y1, y2], 'b')
        plt.savefig(outputfile)

    def get_beam_forces(self):
        """Computes the internal force of each beam
        using csr sparse matrices"""
        self.beam_forces_dict = {}
        nrc = len(self.joint_dict) * 2
        row = []
        col = []
        data = []
        rowb = []
        colb = []
        datab = []
        for i in range(1, len(self.joint_keys) + 1):
            for j in range(1, len(self.beam_keys) + 1):
                if self.beam_keys[j - 1] in self.beams_conn2_joints[i]:
                    row.append(2 * i - 2)
                    col.append(j - 1)
                    data.append(self.beam_coefs[j][0])
                    row.append(2 * i - 1)
                    col.append(j - 1)
                    data.append(self.beam_coefs[j][1])
            if abs(self.joint_dict[i][1][0]) > 0:
                rowb.append(2 * i - 2)
                colb.append(0)
                datab.append(self.joint_dict[i][1][0])
            if abs(self.joint_dict[i][1][1]) > 0:
                rowb.append(2 * i - 1)
                colb.append(0)
                datab.append(self.joint_dict[i][1][1])
        count = 0
        for i in range(1, len(self.joint_keys) + 1):
            if abs(self.joint_dict[i][2][0]) > 0:
                if count == 0:
                    row.append(2 * i - 2)
                    col.append(len(self.beam_keys))
                    data.append(self.joint_dict[i][2][0])
                    row.append(2 * i - 1)
                    col.append(len(self.beam_keys) + 1)
                    data.append(self.joint_dict[i][2][0])
                    count = count + 1
                else:
                    if len(self.beam_keys) + 3 >= nrc:
                        raise RuntimeError("System is overdetermined.")
                    else:
                        row.append(2 * i - 2)
                        col.append(len(self.beam_keys) + 2)
                        data.append(self.joint_dict[i][2][0])
                        row.append(2 * i - 1)
                        col.append(len(self.beam_keys) + 3)
                        data.append(self.joint_dict[i][2][0])
        Asparse = csr_matrix((data, (row, col)), shape=(nrc, nrc))
        Bsparse = csr_matrix((datab, (rowb, colb)), shape=(nrc, 1))
        rank = np.linalg.matrix_rank(Asparse.toarray())
        if rank < nrc:
            raise RuntimeError("System is underdetermined due to unstable geometry.")
        if rank > nrc:
            raise RuntimeError("System is overdetermined.")
        bf = scipy.sparse.linalg.spsolve(Asparse, Bsparse)
        beam_forces = bf[0:len(self.beam_keys)]
        for item in self.beam_keys:
            self.beam_forces_dict[item] = beam_forces[item-1]
        return self.beam_forces_dict

    def __repr__(self):
        """returns the internal force of each beam,
        which represents the Truss class"""
        class_representation = ' Beam       Force\n-----------------\n' +'\n'.join('     %s      %.3f'
                            % (k, v) for k, v in self.beam_forces_dict.items())
        return class_representation

