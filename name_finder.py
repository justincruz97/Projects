# Name: Justin Cruz

import os.path
import sys

def firstLast(file_name):
    with open(file_name) as file:
        name_exists = False
        for line in file:
            low_line = line.casefold()
            if( "name:" in low_line ):
                name_exists = True    
                split_line = low_line.split()
                #print(split_line)
                idx = split_line.index("name:")
                first = split_line[idx + 1].upper()
                last = split_line[idx + 2].upper()
                print("First: %s" %first)
                print("Last: %s" %last)
                break
        if( name_exists == False ):
            print("%s contains no name." %file_name)

# IF INPUT TEXT FILE EXISTS
if ( len(sys.argv) > 1 ):
    input_file = sys.argv[1]
    if( os.path.isfile(input_file) ):
        firstLast(input_file)
    # INPUT FILE DOESN'T EXIST
    else:
        print("%s doesn't exist" %input_file)
# USING DEFAULT ME.TXT
else:
    if( os.path.isfile("me.txt") ):
        firstLast("me.txt")
    else:
        print("\"me.txt\" doesn't exist")



first = 3
second = 20

def swirl(first,second=3):
    first,second = second,first
    return first

result = swirl(swirl(first),second)
result = swirl(second,result)

print(result)
