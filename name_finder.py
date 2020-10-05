# Name: Justin Cruz
# This file will locate a name inside a repository
# and will determine if the file contains a name

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
                idx = split_line.index("name:")
                first = split_line[idx + 1].upper()
                last = split_line[idx + 2].upper()
                print("First: %s" %first)
                print("Last: %s" %last)
                break
        if( name_exists == False ):
            print("%s contains no name." %file_name)
               
def main():
    # if input text file exists
    if ( len(sys.argv) > 1 ):
        input_file = sys.argv[1]
        if( os.path.isfile(input_file) ):
            firstLast(input_file)
            
        # if input file doesn't exist
        else:
            print("%s doesn't exist" %input_file)
            
    # using a default me.txt
    else:
        if( os.path.isfile("me.txt") ):
            firstLast("me.txt")
        else:
            print("\"me.txt\" doesn't exist")

if __name__ == "__main__":
    main()

