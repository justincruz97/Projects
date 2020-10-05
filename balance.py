# Justin Cruz

# This file will look through a file and check if it is correctly balanced.

import os.path
import sys

def fileCheck(input_file):
    stack = []

    with open(sys.argv[1]) as file:
        no_com_name = file.name + ".nocom"
        no_com = open(no_com_name, "w")
        multiline = False
        for line in file:
            # REMOVING "//"
            if( ("//" in line) and (not multiline) ):
                stop = line.index("//")
                no_com.write( line[:stop] + "\n" )
                
            # REMOVING "/*" AND "*/" MULTILINE
            elif( ("/*" in line) and (not multiline) ):
                front = line.index("/*")
                
                # BOTH FRONT AND BACK IN LINE
                if( ("/*" and "*/" in line) == True ):
                    back = line.index("*/")
                    no_com.write( line[:front] + line[back + 2:] )
                
                # ONLY FRONT IN LINE
                else:
                    no_com.write( line[:front] )
                    multiline = True
                    
            elif( ("*/" in line) and multiline):
                front = line.index("*/")
                no_com.write( line[front+2:] )
                multiline = False            

            # NO COMMENTS
            elif( not multiline ):
                no_com.write(line)
        no_com.close()
        
    # BALANCE CHECK
    target = {"{": "}", "[": "]", "(": ")", "}": "{", "]": "[", ")": "("}

    with open(no_com_name) as nc_file:
        for line in nc_file:
            # LINE CONTAINS QUOTES 
            if( "\"" in line ):
                split_line = line.split()
                for split in split_line:
                    start = split.find("\"")
                    end = split.find("\"", start + 1)
                    quote = split[start:end + 1]
                    no_quote = split.replace(quote,"")
                    # ADDING BALANCE PARAMETERS / CHECK
                    for char in no_quote:
                        if( char in target ):
                            stack.append(char)
                            if( len(stack) <= 1 ):
                                continue
                            elif( target.get(stack[-2]) == stack[-1] ):
                                stack.pop()
                                stack.pop()
            # NO QUOTES 
            else:
                for char in line:
                    if( char in target ):
                        stack.append(char)
                        if( len(stack) <= 1 ):
                                continue
                        elif( target.get(stack[-2]) == stack[-1] ):
                            stack.pop()
                            stack.pop()
    if(len(stack) == 0):
        print("File is balanced.")
    else:
        print("File is NOT balanced.")


def main():
    # IF INPUT TEXT FILE EXISTS
    if ( len(sys.argv) > 1 ):
        input_file = sys.argv[1]
        if( os.path.isfile(input_file) ):
            fileCheck(input_file)
            
        # INPUT FILE DOESN'T EXIST
        else:
            print("%s doesn't exist" %input_file)
            
    # NO FILE INPUTTED
    else:
        print("Please input a file.")
        
        
if __name__ == "__main__":
    main()

