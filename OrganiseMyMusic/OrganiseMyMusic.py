import platform
import re
import os

separator = ""

# Decide the directory separator based on the OS
# Also get the partitions to walk through.
def getPartitions():

	drive = []

	if platform.system() == "Windows":
		separator = "\\"
		drives = raw_input("Enter the partitions on your windows machine, separated by a space ")

	 	drives = drives.split(' ')

		for dr in drives:
			if re.match('^[a-z]:\\\\$',dr,re.IGNORECASE):
				drive.append(dr)
			elif re.match("^[a-z]$",dr,re.IGNORECASE):
				dr += ":\\"
				drive.append(dr)
			elif re.match("^[a-z]:$",dr,re.IGNORECASE):
				dr += "\\"
				drive.append(dr)
			else:
				print("Unrecognized option %s, skipping." % dr)

	else:
		separator = "/"
		# Linux is a TODO.
		# SORRY.

	return drive

# Get the partitions, and pass
def musicScan(drives):
	for drive in drives:
		for root, dirs, files in os.walk(drive):
# for all files in directory
			for file in files:
				print root + separator + file

# This is the main module we will use.
def run():
	musicScan(getPartitions())
