This repository contains homework 1 for Amaury Reed, student in CME 211. 

# Part 2 Write Up
For my handwritten test data, I used two common three letter words (with one extra letter at the end) to generate 
the reference file. The three letter words I used were "TAG" and "CAT". Designing my reference file in this way allowed 
me to create reads that satisfied the stated requirements. I repeated the word "TAG" twice in the reference file to make 
it the read that would align twice. The word "CAT" would be one of the reads that aligned once. A important consideraton 
was to ensure that the word "CAT" did not mistakingly align twice with the letters at the end of "TAG" and at the 
beginning of "CAT". 

Given that we are using the random() function to generate random numbers between 0 and 1, we should not
expect an exact 15% / 75% / 10% distribution. While the random() function will generally abide by this 
distribution, it is possible (albeit unlikely) for numbers between 0 and 0.15 to be generated 20% of 
the time, or contrarily, numbers between 15 and 90 to be generated only 65% of the time. It can be considered
tantamount to rolling die or flipping a coin - with enough flips, the coin will land on heads approximately
50% of the time, but not exactly. The same can be said for the random number generator determining the 
interval of the read alignments.

This assignment took me approximately 5 hours. I spent quit abite of time grappling with the each prompt 
and making sure each requirement was met. I also made a few silly errors that took a while to debug. 

## Command Line Log

amauryr@rice11:/farmshare/user_data/amauryr/cme211-reedamaury/hw1$ python3 generatedata.py 1000 600 50 "ref_1.txt" "reads_1.txt"
reference length: 1000
number reads: 600
read length: 50
aligns 0: 0.12666666666666668
aligns 1: 0.785
aligns 2: 0.08833333333333333
amauryr@rice11:/farmshare/user_data/amauryr/cme211-reedamaury/hw1$ python3 generatedata.py 10000 6000 50 "ref_2.txt" "reads_2.txt"       
reference length: 10000
number reads: 6000
read length: 50
aligns 0: 0.16033333333333333
aligns 1: 0.7438333333333333
aligns 2: 0.09583333333333334
amauryr@rice11:/farmshare/user_data/amauryr/cme211-reedamaury/hw1$ python3 generatedata.py 100000 60000 50 "ref_3.txt" "reads_3.txt"     
reference length: 100000
number reads: 60000
read length: 50
aligns 0: 0.16155
aligns 1: 0.7498333333333334
aligns 2: 0.08861666666666666

# Part 3 Write Up
Yes, the distribution of reads that align 0, 1, or 2 or more times in processdata.py, did indeed exactly 
match the distributions computed by the generatedata.py. This is because we are using the exact same reads 
in each script, and therefore the ratio of aligns to the number of reads shoud be constant. If there these
distributions do not match, it means a read was aligned incorrectly. 

Based on the run time data of the program, it can be concluded that this program is not scalable. 
As the size of the reference length grew, the time it took to run the program grew exponentially. 
For the human genome, which is about 3 billion base pairs long, the exponential model I created in 
MATLAB predicted it would probably take on the order of years to run to end. Ultimately, I think it 
is clear that this program would not be sufficient to analyze a complete human genome. 

I spent about 4 hours writing the code for this part. Again, I was really pedantic with understanding exactly
what the prompt was asking for. 

## Command Line Log

amauryr@rice11:/farmshare/user_data/amauryr/cme211-reedamaury/hw1$ python3 processdata.py "ref_1.txt" "reads_1.txt" "align_1.txt"        
reference length: 1000
number reads: 600
aligns 0: 0.16333333333333333
aligns 1: 0.745
aligns 2: 0.09166666666666666
elapsed time: 0.018909692764282227
amauryr@rice11:/farmshare/user_data/amauryr/cme211-reedamaury/hw1$ python3 processdata.py "ref_2.txt" "reads_2.txt" "align_2.txt"        
reference length: 10000
number reads: 6000
aligns 0: 0.15366666666666667
aligns 1: 0.7576666666666667
aligns 2: 0.08866666666666667
elapsed time: 1.4408679008483887
amauryr@rice11:/farmshare/user_data/amauryr/cme211-reedamaury/hw1$ python3 processdata.py "ref_3.txt" "reads_3.txt" "align_3.txt"        
reference length: 100000
number reads: 60000
aligns 0: 0.16013333333333332
aligns 1: 0.75095
aligns 2: 0.08891666666666667
elapsed time: 145.18898701667786
