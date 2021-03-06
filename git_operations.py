#!/usr/bin/python3.6

# This file performs the git operations
# like status, add, commit, push, checkout, pull

import sys, getopt, os

def usage():
    print("Check the following options\n")
    print("-s,--status:                  Display the status")
    print("-a,--add <file_name>:         Add newly created file to the git")
    print("-m,--commit <args>:           Commit the file")
    print("-p,--push:                    Push the file to the git branch")
    print("-c,--check-out <brach_name>:  Change the branch")
    print("-C,--clone:                   Clone the repo")
    print("-l,--pull:                    Pull data")
    print("-r,--rm:                      Removed file or directory")

def get_status():
    os.system("git status")

def remove_file_dir(file_name):
    if os.path.isfile(file_name):
        os.system("git rm " + file_name)
        print("git rm " + file_name)
    elif os.path.isdir(file_name):
        os.system("git rm " + file_name)
        print("git rm " + file_name)
    else:
        print("The file", file_name, "not exit")
        sys.exit(2)

def add_file(file_name):
    if os.path.isfile(file_name):
        os.system("git add " + file_name)
        print("git add " + file_name)
    elif os.path.isdir(file_name):
        os.system("git add " + file_name)
        print("git add " + file_name)
    else:
        print("The file", file_name, "not exit")
        sys.exit(2)

def commit_file(msg):
    print("git commit -m " + '"{}"'.format(msg))
    os.system("git commit -m " + '"{}"'.format(msg))

def push_file():
   os.system("git push")

def get_branch():
    os.system("git branch")

def checkout_branch(brach_name):
    print("git checkout " + brach_name)
    os.system("git checkout " + brach_name)

def clone_repo(repo_name):
    os.system("git clone " + repo_name)

def pull_data():
    os.system("git pull")

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"sa:m:pbc:C:lr:,h",["status","add=","commit=","push","branch","check-out","clone","pull","rm","help"])
        #print("opts", opts)
        #print("args", args)
        if not opts:
            usage()
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-s","--status"):
            get_status()
        elif opt in ("-a","--add"):
            file_name = arg
            if file_name:
                add_file(file_name)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-m","--commit"):
            if arg:
                print(arg)
                commit_file(arg)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-p","--push"):
            push_file()
        elif opt in ("-b","--branch"):
            get_branch()
        elif opt in ("-c","--check-out"):
            if arg:
               checkout_branch(arg)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-C","--clone"):
            print(opt)
            print(arg)
            if arg:
                clone_repo(arg)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-l","--pull"):
            pull_data()
        elif opt in ("-r", "--rm"):
            file_name = arg
            remove_file_dir(file_name)
        elif opt in ("-h","--help"):
            usage()



if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except OSError as err:
      print("OS error: {0}".format(err))

