import platform
import re
import os
from id3py import ID3
from id3py.ID3 import *
from helpers import move, destdir

# Decide the directory separator based on the OS
# Also get the partitions to walk through.
def getPartitions():

    global separator
    drive = []

    if platform.system() == "Windows":
        separator = "\\"
        drives = raw_input("Enter the partitions or directories you'd like to search on your windows machine, separated by a space: ")
        # #raw
        print("\n")

        drives = drives.split(' ')

        for dr in drives:
            if re.match('^[a-z]:\\\\[a-z]+\\$',dr,re.IGNORECASE):
                drive.append(dr)
            elif re.match("^[a-z]$",dr,re.IGNORECASE):
                dr += ":\\"
                drive.append(dr)
            elif re.match("^[a-z]:$",dr,re.IGNORECASE):
                dr += "\\"
                drive.append(dr)
            else:
                drive.append(dr)
        
        destdir()
    else:
        separator = "/"
        # Linux is a TODO.
        # SORRY.

    return drive


def sort(current, id3tags):
    move(current, id3tags)
#   print current, id3tags, "\n"

def getID3(curfile):
    id3tags = ID3(curfile).as_dict()
    return id3tags


# Get the partitions, and pass
def musicScan(drives):

    for drive in drives:
        
        if os.path.isdir(drive) == False:
            print "Could not find " + drive + ", skipping."
            continue

        for root, dirs, files in os.walk(drive):
            # for all files in directory
            for file in files:
                curfile = root + separator + file

                ext = os.path.splitext(curfile)[-1].lower()
                
                if ext == ".mp3":
                    sort(curfile, getID3(curfile))


# This is the main module we will use.
def run():
    musicScan(getPartitions())