#!/usr/bin/env python3
#Author ID: 104415211

def add(number1, number2):
    try:
        result = int(number1) + int(number2)
        return result  
    except:
        error = 'error: could not add numbers'
        return error

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            lst = f.readlines()
            return lst
    except:
        error = 'error: could not read file'
        return error 



if __name__ == '__main__':
    print(add(10,5))                        
    print(add('10',5))                      
    print(add('abc',5))                     
    print(read_file('seneca2.txt'))         
    print(read_file('file10000.txt'))
