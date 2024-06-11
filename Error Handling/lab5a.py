#!/usr/bin/env python3
#Author ID: 104415211

def read_file_string(file_name):
    with open(file_name, 'r') as f:
        read_data = f.read()
        return read_data
    
def read_file_list(file_name):
    with open(file_name, 'r') as f:
        data = f.read().strip().split('\n')
        return data 

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name)) 