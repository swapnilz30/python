#!/usr/bin/python3.6

# This script getopts method

import sys, getopt

def info_msg():
    print ("getopts.py -i <inputfile -o outputfile>")
    exit(1)

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile=","help"])
        print("opts", opts)
        print("args",args)
        if not opts:
            info_msg()
    except getopt.GetoptError:
        info_msg()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            info_msg()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o","--ofile"):
            outputfile = arg

    print ("Input file is", inputfile)
    print ("Output file is", outputfile)

if __name__  == "__main__":
    main(sys.argv[1:])


