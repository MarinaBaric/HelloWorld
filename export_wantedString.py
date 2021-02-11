# Description: A script to export wanted lines from file
# Usage: c:\Python27\Scripts>export_wantedString.py "String to export" "Path to the file to modify"

import os
import sys

def usage():
    print('Usage: %s pathToLog stringToExport ' % sys.argv[0])
    print('     pathToFile is the path to the logfile to be modified')
    print('     stringToExport is a string that is contained in the lines to export')
    

if len(sys.argv) < 3:
        usage()
        exit(1)

wantedString = sys.argv[1]
pathToFile = sys.argv[2]


newFile = open(pathToFile + "_MODDED",'w')
newFile.write("This is a modified version of: " + pathToFile + '\n')
newFile.write("Where lines not containing the string: " + wantedString + " have been removed." + '\n')
newFile.write('\n')

##line.split("=",1)[1]
for line in open(pathToFile):
    if wantedString in line:
        newFile.write(line)

newFile.close()
