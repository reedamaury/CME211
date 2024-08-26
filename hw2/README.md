This repository contains homework 2 for Amaury Reed, student in CME 211. 


Part 1 Write Up

1. My primary consideration when creating the test data was to test my code in all three cases: -1 correlations, 1 correlation, and 0 correlation. Thus, I partitioned the data set into thirds. The first third of the dataset was intended to test the -1 correlation case, the second third was intended to test the 1 correlation case, and the final third was intended to test the 0 correlation case. 

2. While my data was less random and more finely partitioned than the real data, I would still say it bears resemblance to real data, in that it tests corner cases and ensures the efficacy of the program

3. I did manually write out a reference solution and it helped quite a bit with debugging. The reference solution simply contained the average rating for each movie and the maximum correlation for each movie.


Part 2 Write Up

When incorporating functions into a program, my primary objective is to eliminate repetition. When I find myself repeating some operation multiple times, I begin to imagine ways I can create an overarching function to eliminate the redundancy in an effective manner. For this program, I think that programming philosophy is best exemplified by my newdict() function. I found myself frequently needing to create dictionaries to associate containers of data, so to reduce the complexity of the code, maintain brevity, and avoid repetition, I created a function to do this. I also wrote functions to carry out simple, redundant mathematical operations. 

Command line logs
amauryr@rice05:/farmshare/user_data/amauryr/cme211-reedamaury/hw2$ python similarity.py test.data blank.txt [user_thresh default = 5]
Input MovieLens file: test.data
Output file for similarity data: blank.txt
Minimum number of common users: 5
Read 20 lines with total of 3 movies and 10 users
Computed similarities in 0.000 seconds
amauryr@rice05:/farmshare/user_data/amauryr/cme211-reedamaury/hw2$
