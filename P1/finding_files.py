
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    for file in os.listdir(path):
        #print (file)
        #print (str(file).endswith(".py"))
        if str(file).endswith(".py"):
            files.append(file)
        if file.isdir:
            print ("Dir " + file)


    
    return files

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./Task4.py"))

# Does the file end with .py?
print ("./Task4.py".endswith(".py"))

file_c = find_files("py",".")

print (file_c)
