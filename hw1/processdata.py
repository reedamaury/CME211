import sys
import string
import time

# ensure correct number of input arguments
if len(sys.argv) < 4:
    print("Usage Error: not enough command line arguments")
    quit()

# initialize variables
reffile = open(sys.argv[1],"r")
readfile = open(sys.argv[2],"r")
reference = reffile.read()
reads = readfile.readlines()
readlen = len(reads)
reflen = len(reference)
output_string = []
align0 = 0
align1 = 0
align2 = 0
t1 = time.time()                                             # starts timer to record run time of program
for i in range(readlen):
    r = reads[i]
    read = r.strip("\n")                                     # removes the \n in each line
    ind = reference.find(read)                               # finds the first index where read aligns to reference
    if ind < 0:                                              # if index is less than 0 (-1), it has no alignment
        align0 += 1                                          # alignment counter
        output_string.append("{} {}".format(read, ind))      # adds read and indices of alignment to the list
    elif ind >= 0:
        ref = list(reference)                              # unpacks reference string - puts each letter into individual indices of list
        refn = ref[ind+1:]                                   # creates a new reference to find second alignment
        refnew = ''.join(refn)                               # coverts list into one string
        indx = refnew.find(read)                             # finds the second index where read aligns to reference
        if indx < 0:                                         # if index is less than 0 (i.e. -1), it has two alignments
            align1 +=  1                                     # alignment counter
            output_string.append("{} {}".format(read,ind))   # adds read and indices of alignment to the list
        elif indx >= 0:                                      # if index is in great than or eqaul to 0 (not -1), it has one alignment
            ind2 = indx + ind                                # calculates index of alignment with respect to entire reference
            align2 += 1                                      # alignment counter
            output_string.append("{} {} {}".format(read,ind,ind2)) # adds read and indices of alignment to the list
t2 = time.time()
# end timer
# write each read with it's corresponding index/indices to alignment file
output_string = "\n".join(output_string)
with open(sys.argv[3], 'w') as f:
    f.writelines(output_string)

# calculate percentage of 0, 1, and 2 alignments
align01 = align0/len(reads)
align11 = align1/len(reads)
align21 = align2/len(reads)
print("reference length: {}".format(reflen))
print("number reads: {}".format(readlen))
print("aligns 0: {}".format(align01))
print("aligns 1: {}".format(align11))
print("aligns 2: {}".format(align21))
print("elapsed time: {}".format(t2-t1))
