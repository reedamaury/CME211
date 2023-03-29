import itertools
import math
import string
import sys
import time


# Functions
# Convert list to tuple
def convert(list):
    return tuple(list)

# Create Dictionary
def newdict(key, value):
    dictname = {}
    for i in range(len(key)):
        if key[i] not in dictname:              #if user does not exist already, create new one
            dictname[key[i]] = [value[i]]
        else:                                   #if user exist already, append more values to it
            dictname[key[i]].append(value[i])
    return dictname

# Find Mean
def mean(L):
    return sum(L)/len(L)

# Find Difference
def dif(r1,r2):
    return r1-r2

# Ensure correct number of input arguments
if len(sys.argv) < 6:
    print("Usage Error: not enough command line arguments")
    quit()


# Define last command line argument
s = str(sys.argv[6])
thresh = ""
for letter in s:
    if letter.isdigit():
        thresh = thresh + letter
thresh = int(thresh)


# Open Movie Lens and create a tuple
datfile = open(sys.argv[1],"r")
numlines = datfile.readlines()
newlines= [l.split() for l in numlines]
a = newlines
a = list(zip(*a))
#a = list(map(list, itertools.zip_longest(*a, fillvalue=None)))

# Initialize keys and values)
key = a[0]
movies = a[1]
ratings = a[2]
key = tuple(map(int,key))
movies = tuple(map(int, movies))
ratings = tuple(map(int, ratings))


# Assign each user a respective movie and rating via a dictionary. Also assign movies ratings
user_movies = newdict(key, movies)
user_ratings = newdict(key, ratings)
movie_ratings = newdict(movies, ratings)
num_movies = len(movie_ratings)
key = set(key)
key = tuple(key)
movies = set(movies)
movies = tuple(movies)


# Initialize dictionaries
movie_similarities = {}
movie_match = {}
movie_users = {}
movie_maxsim = {}
movie_count = {}
tup_print = {}



# Compute Similarities

t1 = time.time()
for i in range(num_movies):
    ri_bar = mean(movie_ratings[movies[i]]) # Compute average rating for each movie
    for j in range(num_movies-1):
        rnum = 0
        r1 = 0
        r2 = 0 
        count = 0   
        for k in range(len(user_movies)):
            if movies[i] and movies[j+1] in user_movies[key[k]]: # if user has rated both movies proceed
                rij_bar = mean(movie_ratings[movies[j+1]])
                ri = user_ratings[key[k]][0]
                rij = user_ratings[key[k]][1]
                rnum = dif(ri,ri_bar)*dif(rij, rij_bar) + rnum
                r1 = dif(ri,ri_bar)**2 + r1
                r2 = dif(rij,rij_bar)**2 + r2
                count = count + 1  # every time a user has rated both movies increase counter
        if count >= int(thresh): # if more than 4 users rated both movies assign it a similarity
            if rnum == 0:  # check if denom will be 0
                P = 0
            else:
                P = rnum/math.sqrt(r1*r2)

            if movies[i] not in movie_similarities:
                movie_similarities[movies[i]] = [P]
                movie_match[movies[i]] = [movies[i+j]]
                movie_count[movies[i]] = [count] # store how many users rated both movies
            else:
                movie_similarities[movies[i]].append(P)
                movie_match[movies[i]].append(movies[1+j])
                movie_count[movies[i]].append(count)

    if movies[i] not in movie_similarities: #after iterating through all movies, if movie has no match, gets []
        movie_similarities[movies[i]] = []
        movie_match[movies[i]] = []
        movie_count[movies[i]] = []
        movie_maxsim[movies[i]] = []
        tup_print[movies[i]] = []
    else:
        movie_maxsim[movies[i]] = (max(movie_similarities[movies[i]]))
        tup_print[movies[i]] = (movie_match[movies[i]][0],\
                               round(movie_maxsim[movies[i]],2),movie_count[movies[i]][0])
t2 = time.time()
t = t2-t1

# Sort dictionary to be written to output file
tup_print_sort = dict(sorted(tup_print.items()))
with open(sys.argv[2], 'w') as f:
    for k, v in tup_print_sort.items():
        f.write('%s %s\n' % (k, v))


print('Input MovieLens file: {}'.format(sys.argv[1]))
print('Output file for similarity data: {}'.format(sys.argv[2]))
print('Minimum number of common users: {}'.format(thresh))
print('Read {} lines with total of {} movies and {} users'.format(len(ratings),len(movies),len(user_movies)))
print('Computed similarities in {:.3f} seconds'.format(t))
