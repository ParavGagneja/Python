#!/usr/bin/env python3

import subprocess, sys
import os
import argparse



'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: "Parav Gagneja"
The python code in this file (duim.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: This srcipt gonna generate the output which will represent the percentage of space used by directory 
             through graph in addition it will depict the absolute path of directory

Date: Dec 9, 2022
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2022")



    #parser.add_argument("-h", "--help", action= "store_true")
    
    
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    parser.add_argument('-H', '--human-readable', action='store_true',help='print sizes in human readable format (e.g. 1K 23M 2G)')

    # add argument for length of charcters
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")


    # add argument for "target". set number of args to 1.
    current_dir = os.popen('pwd')
    t1 = current_dir.read()
    parser.add_argument('target', nargs='*',default = t1,help='The directory to scan.')

    
    # To avoid any extra size of files which are not required
    parser.add_argument("-t", "--threshold", type=str, default='',help='results that are less than a user-specified size get excluded from results.')
    
    
    args = parser.parse_args()
    

    return args 
    


def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    if percent not in range(0, 101):
        return 'Error :Value of percent must lies between 0 to 100'
    else:
        # N is the no of equal signs present in graph
        N = int(round((percent * total_chars) / 100))
        
        # S represents the number of spaces
        S = total_chars - N

        sign = '='
        space = ' '

        # out is the string output without any brackets
        out = (str(sign) * N) + (str(space) * S)

        # graph is the final output and the return value
        graph = '[' + out + ']'
        return graph  

def call_du_sub(location):
    "takes the target directory as an argument and returns a list of strings"
    "returned by the command `du -d 1 location`"
    a =subprocess.Popen(['du -d 1 '+ location], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output= a.communicate()
    x = output[0].decode('utf-8').strip().split()
    return x 


def create_dir_dict(alist):
    "gets a list from call_du_sub, returns a dictionary which should have full"
    "directory name as key, and the number of bytes in the directory as the value."
    dir = {}
    for x in alist:
        m = alist.index(x)
        if m in range(0, len(alist)-1, 2):
            dir[x] =  alist[m + 1]

    
    dir_swap = dict(zip(dir.values(), dir.keys()))

    return dir_swap  



    
def per_cent(location):
    args = parse_command_args()

    list_of_subd = call_du_sub(location)
    dic_subd = create_dir_dict(list_of_subd)

    for item in dic_subd.values():
        val = os.popen('df ' + location)
        total = val.read()

        pc = (item / total) * 100

        return pc  
    

def conversion(location):
    list_of_subd = call_du_sub(location)
    dic_subd = create_dir_dict(list_of_subd)

    result = os.popen('du -h '+ dic_subd.keys)
    last = result.read()

    return last 



if __name__ == "__main__":
    args = parse_command_args()
    location = args.target
    list_of_subd = call_du_sub(location)
    dic_subd = create_dir_dict(list_of_subd)
    
    n = per_cent() + '%'

    a = per_cent 
     
    t = args.length

    k = dic_subd.values()
    output = n + percent_to_graph(a, t) + conversion(k)

