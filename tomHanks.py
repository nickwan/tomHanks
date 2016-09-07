
# coding: utf-8

# In[86]:

# This is a super ugly code to mine the data from the TomHanksTop5 hashtag.
# Thanks to Justin Kiggins (twitter: @neuromusic) for getting the tweets out into JSON!

import os, json
import re
import numpy as np
import pandas as pd

# lists all the tweets
path_to_json = '/Users/leapnirs/Downloads/tweets/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
movieRanks = np.array(['Movie', 'Score'])

# Super ugly nested for
for y in json_files:
    t = json.loads(open("/Users/leapnirs/Downloads/tweets/"+y).read())
    splitText = t['text'].split('\n') # First splits lines

    for x in splitText:
        try: 
            if re.search('^1[\\W]+',x): # seeks out a numbered bullet
                movieSplit = re.split('[.:-]\s*',x) # splits again at the numbered bullet; I know, this leaves out data that aren't numbered...
                temp = np.array([movieSplit[1],100]) # holds the line, split by delimiter, in a variable; normalizes 5-point scale to 100 pts
                movieRanks = np.vstack((movieRanks, temp)) # concatenates on existing array
            elif re.search('^2[\\W]+',x):
                movieSplit = re.split('[.:-]\s*',x)
                temp = np.array([movieSplit[1],80])
                movieRanks = np.vstack((movieRanks, temp))
            elif re.search('^3[\\W]+',x):
                movieSplit = re.split('[.:-]\s*',x)
                temp = np.array([movieSplit[1],60])
                movieRanks = np.vstack((movieRanks, temp))
            elif re.search('^4[\\W]+',x):
                movieSplit = re.split('[.:-]\s*',x)
                temp = np.array([movieSplit[1],40])
                movieRanks = np.vstack((movieRanks, temp))
            elif re.search('^5[\\W]+',x):
                movieSplit = re.split('[.:-]\s*',x)
                temp = np.array([movieSplit[1],20])
                movieRanks = np.vstack((movieRanks, temp))
        except Exception: # this code runs into tons of errors (I told you it was uggo)
            pass

headers = movieRanks[0] # will use the first row as headers
movieRanks = pd.DataFrame(data=movieRanks[1:]) # clears the header, converts to dataframe (slightly unnecessary, but whatevs)
movieRanks.columns = headers 
movieRanks.to_csv('/Users/leapnirs/Desktop/movies/Tom Hanks/movieRanks.csv')
# This exports about 40% of the available data; someone more pythonic than I could probably get that number higher :(

