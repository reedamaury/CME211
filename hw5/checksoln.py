import numpy as np
import sys

# initialize solution and maze files from command line arguments
solution_file = sys.argv[2]
maze_file = sys.argv[1]

# read solution and maze files
with open(solution_file, 'r') as f:
    fline = f.readlines()[0:]
    new = [s.strip('\n') for s in fline]
    split_lines = [l.split() for l in new]
    solution = list(map(list, zip(*split_lines)))
    solutionrow_idx = [int(i) for i in solution[0]]
    solutioncol_idx = [int(i) for i in solution[1]]
    f.close()

with open(maze_file, 'r') as fo:
    colsplit = [column.split() for column in fo]
    first = colsplit[0]
    rc = [int(i) for i in first]
    fo.close()

with open(maze_file, 'r') as fm:
    next(fm)
    flines = fm.readlines()
    split_lines = [l.split() for l in flines]
    mazeidx_string = list(map(list, zip(*split_lines)))
    mazerow_idx = [int(i) for i in mazeidx_string[0]]
    mazecol_idx = [int(i) for i in mazeidx_string[1]]
    fm.close()

# construct maze
maze = np.zeros((rc[0],rc[1]), dtype=np.int8)
for i in range(len(mazerow_idx)):
    maze[mazerow_idx[i]][mazecol_idx[i]] = 1

# find entrance and exit of maze
maze_dict = {}
for i in range(rc[1]):
    if maze[0][i] == 0:
        maze_dict["entrance"] = [0,i]
        break
for i in range(rc[1]):
    if maze[rc[0]-1][i] == 0:
        maze_dict["exit"] = [rc[0]-1,i]
        break

# confirm that solution entered the maze at the correct location
if solutionrow_idx[0] != maze_dict["entrance"][0] or solutioncol_idx[0] != maze_dict["entrance"][1]:
    print("Solution not valid! You did not enter the maze at the correct location.")
    sys.exit()

# confirm that solution does not go through any walls
for i in range(len(solutioncol_idx)):
    if maze[solutionrow_idx[i]][solutioncol_idx[i]] != 0:
        print("Solution not valid! You went through a wall.")
        sys.exit()

# confirm each move is valid, meaning you can only move to adjacent cells
for i in range(len(solutioncol_idx)-1):
    row_dif = solutionrow_idx[i] - solutionrow_idx[i + 1]
    col_dif = solutioncol_idx[i] - solutioncol_idx[i + 1]
    if abs(row_dif) != 1 and abs(col_dif) != 1:
        print("Solution not valid! All moves were not adjacent!")
        sys.exit()

# confirm that solution exited the maze at the correct location
exitrow_solnidx = len(solutionrow_idx)-1
exitcol_solnidx = len(solutioncol_idx)-1
if solutionrow_idx[exitrow_solnidx] != maze_dict["exit"][0] or solutioncol_idx[exitcol_solnidx] != maze_dict["exit"][1]:
    print("Solution not valid! You did not exit the maze at the correct location.")
    sys.exit()

# if conditions above are not violated, the solution is valid
print("Solution is valid!")
