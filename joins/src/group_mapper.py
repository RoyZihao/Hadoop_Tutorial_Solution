#!/usr/bin/env python
# map function for matrix multiply


import os
import sys

# determine which file are we reading
A = False
T = False

# Hadoop may break each input file into several small chunks for processing
# and the streaming mode only shows us one row (line of text) at a time.
#
# If we want to know what file the input data is coming from, this is
# stored in the environment variable `mapreduce_map_input_file`:
if 'artist' in os.environ['mapreduce_map_input_file']:
    A = True
elif 'track' in os.environ['mapreduce_map_input_file']:
    T = True
else:
    raise RuntimeError('Could not determine input file!')

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Split line into array of entry data
    entry = line.split(",")

    # If this is an entry in artist_term...
    if A:
        # Generate the necessary key-value pairs
        artist_id = entry[0]
        term = entry[1]
        print('{}\t{},{}'.format(artist_id,'artist_term',1))
        ###

        pass
    # Otherwise, if this is an entry in matrix B...
    else:
        # Generate the necessary key-value pairs
        artist_id = entry[-1]
        year = entry[3]
        duration = entry[-2]
        print('{}\t{},{},{}'.format(artist_id,'track',year,duration))

        pass
