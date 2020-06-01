#!/usr/bin/env python


import sys
from itertools import product

# Create data structures to hold the current row/column values 

###
# (if needed; your code goes here)
###
current_key = None
cur_artist = []
cur_track = []


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Get key/value and split by tab
    key, value = line.split('\t', 1)

    # Parse key/value input (your code goes here)
    try:
        value = value.split(',')
        table = value[0]

    except ValueError:
        # if element split fails, silently
        # ignore/discard this line
        continue

    # If we are still on the same key...
    if key == current_key:

        # Process key/value pair
        if table == 'artist_term':
            cur_artist.append(value)
        else:
            cur_track.append(value)


        
    # Otherwise, if this is a new key...
    else:
        # If this is a new key and not the first key we've seen
        #compute/output result to STDOUT
        if current_key:
            if cur_track:
                years = [int(i[1]) for i in cur_track]
                max_year = max(years)
                durations = [float(i[-1]) for i in cur_track]
                avg_dur = sum(durations) / len(durations)

                if cur_artist:
                    num_term = 0
                    for j in range(len(cur_track)):
                        num_term += sum([int(i[1]) for i in cur_artist])
                else:
                    num_term = 0
                print('{},{},{},{}'.format(current_key,max_year,avg_dur,num_term))

            cur_artist = []
            cur_track = []


        current_key = key

        # Process input for new key
        if table =='artist_term':
            cur_artist.append(value)
        else:
            cur_track.append(value)
        
    
        pass



#Compute/output result for the last key

###
# (your code goes here)
if current_key: 
    if cur_track:
        years = [int(i[1]) for i in cur_track]
        max_year = max(years)
        durations = [float(i[-1]) for i in cur_track]
        avg_dur = sum(durations) / len(durations)

        if cur_artist:
            num_term = 0
            for j in range(len(cur_track)):
                num_term += sum([int(i[1]) for i in cur_artist])
        else:
            num_term = 0
        print('{},{},{},{}'.format(current_key,max_year,avg_dur,num_term))

###

