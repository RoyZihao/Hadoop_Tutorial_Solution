#!/usr/bin/env python
from __future__ import print_function
#Reduce function for computing matrix multiply A*B

import sys
import os
import string
import numpy as np

# We should pay special attention to the occasion that
# no artist_id linked to track_id or no track_id linked to artist_id

#SELECT 	artist_id, track_id, term
#FROM	track INNER JOIN artist_term 
#ON 		track.artist_id = artist_term.artist_id

current_key = None
track_list = []
term_list = []
#count = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t', 1)
    
    # Parse key/value input (your code goes here)
    value = value.replace(' ','')
    value = value.replace('(','')
    value = value.replace(')','')
    value = value.replace("'",'')
    value = value.split(',')
    #print('Read in key:',key)
    #print('Read in value:',value)
    
# If we are still on the same key...
    if key == current_key:

        # Process key/value pair
        ###
        if value[0] == 'track':
            track_list.append(value[1])
        else:
            term_list.append(value[1])


    # Otherwise, if this is a new key...
    else:
        # If this is a new key and not the first key we've seen
        if current_key:
            # Evaluate whether there exist both term and track_id associated with this artist_id
            if(len(term_list)>0) and (len(track_list)>0):
                #print('\n')
                #print('!!!!!Start to print out the result!!!!')
                for track in track_list:
                    for term in term_list:
                        print('{},{},{}'.format(current_key,track,term))
            

            #compute/output result to STDOUT

            ###
    
        current_key = key
        track_list = []
        term_list = []
        # Process input for new key

        ###
        if value[0] == 'track':
            track_list.append(value[1])
        else:
            term_list.append(value[1])



#Compute/output result for the last key

###
# Evaluate whether there exist both term and track_id associated with this artist_id
if(len(term_list)>0 and len(track_list)>0):
    for track in track_list:
        for term in term_list:
            print('{},{},{}'.format(current_key,track,term))
###

