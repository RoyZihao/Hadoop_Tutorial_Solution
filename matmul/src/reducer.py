#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

import sys

# Create data structures to hold the current row/column values

###
# (if needed; your code goes here)

current_node = 0.0
value_dict = dict()
###


current_key = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Get key/value and split by tab
    key, value = line.split('\t', 1)
    
    # Parse key/value input (your code goes here)
    try:
        row, col = map(int, key.split(','))
        value = value.split(',')
        key = (row,col)
        a_col_b_row, entry_value = int(value[0]), float(value[1])
    except:
        continue


    # If we are still on the same key...
    if key == current_key:
        
        # Process key/value pair
        
        ###
        # (your code goes here)
        if a_col_b_row not in value_dict:
            value_dict[a_col_b_row] = entry_value
        else:
            value_dict[a_col_b_row] *= entry_value
        ###
        
        pass

# Otherwise, if this is a new key...
    else:
        # If this is a new key and not the first key we've seen
        if current_key:
            
            #compute/output result to STDOUT
            
            ###
            # (your code goes here)
            current_node = sum(value_dict.values())
            print('{0:d},{1:d},{2:f}'.format(current_key[0], current_key[1], current_node))
            ###
            
            pass
        
        current_key = key

        # Process input for new key

        ###
        # (your code goes here)
        value_dict = dict()
        value_dict[a_col_b_row] = entry_value
        current_node = 0.0
        ###

        pass



#Compute/output result for the last key

###
# (your code goes here)
if current_key:
    current_node = sum(value_dict.values())
    print('{0:d},{1:d},{2:f}'.format(current_key[0], current_key[1], current_node))
