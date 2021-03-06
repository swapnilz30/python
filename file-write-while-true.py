#!/usr/bin/python3.6

# This script writes the continuous to the file.
# This script is ready but need to handle the keyboard interrupt

import os
from sys import exit


# Check the input object is dir or file.
def check_input(ifile):
    global file_status
    if os.path.isdir(ifile):
        print("The ", ifile, "is directory")
        exit()
    elif os.path.isfile(ifile):
          file_status = 1
    else:
          file_status = 0

# Check the file exist or not.
def file_write(ifile):
     if file_status == 0:
         try:
           print ("The ",ifile,"file created.")
           ofile = open(ifile,'w')
           line = input("Enter lines\n")
           while (True):
               ofile.write(ifile)
               line = input()
         finally:
             print ("The file", ifile,"successfully written")
             ofile.close()

     else:
        try:
          print("The ", ifile,"exist")
          flag = input("Do you wish to over write (a/y/n): ")
          if flag == "a":
             ofile = open(ifile, 'a')
             line = input("Enter lines\n")
             while (True):
                 ofile.write(ifile)
                 line = input()
          elif flag == "y":
             ofile = open(ifile, 'w')
             line = input("Enter lines\n")
             while (True):
                 ofile.write(ifile)
                 line = input()
          else:
             exit()
        finally:
          ofile.close()

#### Main ####

ifile = input("Enter the file name: ")

check_input(ifile)
file_write(ifile)




# Take continuous input from the user.
# Write to the file.

# close the file.
