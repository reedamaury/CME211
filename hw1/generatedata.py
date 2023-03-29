import string
import sys
import random

# ensure correct number of input arguments
if len(sys.argv) < 6:
    print("Usage Error: not enough command line arguments")
    quit()

# generate reference file

# initialize variables
reflen = int(sys.argv[1])
numread = int(sys.argv[2])
readlen = int(sys.argv[3])
reffile = sys.argv[4]
readfile = sys.argv[5]
ref = []
lst = ['A','T','G','C']                     # list of letters we want to occur randomly in reference
reflen_75 = int(reflen*0.75)                # integer 75% of the reference length z

for i in range(reflen_75):                  # for loop to generate random reference list
    n = random.randint(0,3)                 # generates random integer between 0 and 3
    ref.append(lst[n])                      # selects random letter in lst to append to reference
reflen_25 = reflen - reflen_75              # integer 25% of the reference length
reflen_50 = reflen_75 - reflen_25           # integer 50% of the reference length
ref_txt = ref + ref[reflen_50:reflen_75]    # last 25% get added to create the full reference
ref_txtf = ''.join(ref_txt)                 # convert reference list into one string of letters
with open(str(reffile), 'w') as f:          # writes reference string to reference file
    f.write(ref_txtf)

# generate read files

# initialize variables
noreads = 0
tworeads = 0
oneread = 0
read = list(range(numread))                             # initialize read list
for j in range(numread):                                # for loop to generate read list
    v = int(random.random()*100)                        # generates random integer between 1 and 100
    if v > 15 and v <= 90:                              # if the number is between 15 and 90 (75% of interval), read aligns once
        ind = random.randint(0,reflen_50)               # for read to align once to reference, choose random index in first 50%
        m = ref_txt[ind:ind+readlen]                    # use index and read length to create a read list
        read[j] = ''.join(m)                            # convert the read list to a string
        oneread += 1                                    # alignment counter
    if v > 90 and v <= 100:                             # if the number is between 90 and 100 (10% of interval), read aligns twice
        ind = random.randint(reflen_75,reflen-readlen)  # for read to align twice to reference, choose random index in last 25%
        m = ref_txt[ind:ind+readlen]                    # use index and read length to create a read list
        read[j] = ''.join(m)                            # convert the read list to a string
        tworeads += 1                                   # alignment counter
    if v >= 0 and v <= 15:                              # if the number is between 0 and 15 (15% of interval), read does not align
        m = []                                          # initialize empty list, create a random read that does not align with reference
        match = 1                                       # initialize while loop flag
        while match > 0:                                # match will be -1 when read does not align to break while loop
            for k in range(readlen):
                n = random.randint(0,3)                 # generates random integer between 0 and 3
                m.append(lst[n])                        # using random number n, selects letter in list to append to reference
            l = ''.join(m)                              # selects random letter in lst to append to reference
            match = ref_txtf.find(l)                    # match will be -1 when read does not align to break while loop
        read[j] = ''.join(m)                            # convert the read list to a string
        noreads += 1                                    # alignment counter

read_txt = '\n'.join(read)                              # convert read list into string joined by new line
with open(str(readfile), 'w') as f:
    f.write(read_txt)                                   # write each read to new line in read file

align0 = noreads/numread                                # calculate percentage of 0, 1, and 2 alignments
align1 = oneread/numread
align2 = tworeads/numread
print("reference length: {}".format(reflen))
print("number reads: {}".format(numread))
print("read length: {}".format(readlen))
print("aligns 0: {}".format(align0))
print("aligns 1: {}".format(align1))
print("aligns 2: {}".format(align2))
