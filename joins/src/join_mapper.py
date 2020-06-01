#!/usr/bin/env python
from __future__ import print_function
#Reduce function for computing matrix multiply A*B

import sys
import os
import string
import numpy as np
# are we reading a track.csv or an artist_term.csv file?
READING_track = False
READING_artist_term = False

# Hadoop may break each input file into several small chunks for processing
# and the streaming mode only shows us one row (line of text) at a time.
#
# If we want to know what file the input data is coming from, this is
# stored in the environment variable `mapreduce_map_input_file`:
if 'track' in os.environ['mapreduce_map_input_file']:
    READING_track = True
elif 'artist_term' in os.environ['mapreduce_map_input_file']:
    READING_artist_term = True
else:
    raise RuntimeError('Could not determine input file!')

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    # Remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    # Split line into array of entry data
    entry = line.split(",")
    #print(entry)

    # If this is an entry in track...
    if READING_track:
        # Generate the necessary key-value pairs
        #TRACK_ID,title string,album string,year,duration,ARTIST_ID
        ###
        # (your code goes here)
        track_id = entry[0]
        title = entry[1]
        album = entry[2]
        year = entry[3]
        duration = entry[4]
        artist_id = entry[5]
        ###
        key = artist_id
        value = ('track',track_id)
        print('{}\t{}'.format(key, value))

    # Otherwise, if this is an entry in artist_term...
    else:
        # Generate the necessary key-value pairs

        ###
        # (your code goes here)
        artist_id = entry[0]
        term = entry[1]
        ###
        key = artist_id
        value = ('term',term)
        ###
        print('{}\t{}'.format(key, value))
        

