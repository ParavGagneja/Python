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

def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as f:
        new_data = f.write(string_of_lines)
        return new_data 

def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as f:
        for item in list_of_lines:
            f.write(item + '\n')
            
def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as f:
        with open(file_name_write, 'w') as p:
            new = f.read().strip().split('\n')
            number = 1
            for item in new:
                p.write(str(number) + ':' + str(item) + '\n')
                number +=1




if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))