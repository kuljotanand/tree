#!/usr/bin/env python3
import subprocess
import sys


# YOUR CODE GOES here
#Full discretion: I referenced osawill's submission because I was incredibly stuck
import os

things_on_left = []
begin = ""
total_number_of_dir = 0
total_number_of_files = 0

def print_file(filename, depth, last=False, prev_lvl=0):
    spacing = ("  " * prev_lvl) + ('|  ' * (depth - prev_lvl))
    if(last):
        indent = spacing + '|__'
    else:
        indent = spacing + '|--'
    print(indent + basename(filename))

def print_directory(root, depth=0, last=False, parent=0):
    dir_num = 0
    file_num = 0
    components = listdir(root) #listdir is a method on OS library
    components.sort()
    if (depth==0):
        if (root[-1] == '/'):
            root = root[:1]
        print(root)
    else: #now, this is where we have gone past root
        dir_num = dir_num + 1
        if(last):
            print (("  " * (parent - 1)) + ("|  " * (depth - parent - 1)) + '|__' + basename(root))
        else:
            print (("  " * (parent)) + ( "|  " * (depth - parent - 1)) + '|__' + basename(root))

    for i, component in items_in_dir(components):
        component = root + '/' + component
        if (i == len(components) - 1):
            flag = True
            if(isdir(item)):
                parent = depth + 1
            else:
                flag = False

        if(isdir(item)):
            (a,b) = print_directory(item, depth + 1, flag, parent)
            dir_num += a
            file_num += b
        else:
            print_file(component, depth, flag, parent)
            file_num += 1

    return (dir_num, file_num)


if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
