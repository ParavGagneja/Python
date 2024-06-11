#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2022

Program: assign1.py
Author: "Parav Gagneja" - "104415211"

The python code in this file (assign1.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: uploaded both a1_pgagneja.py & a1_output.txt on blackboard

Date: 2022-10-21
'''

import sys

def usage():
    "return a string describing the usage of the script"
    print("Usage: assign1.py DD-MM-YYYY N")

def leap_year(year):
    if len(str(year)) != 4:
        return 'YYYY'
    else:
        lyear = int(year)
        if (lyear % 4 == 0 and lyear % 100 != 0) or lyear % 400 == 0: 
            return True        
        else:
            return False 

def days_in_mon(year):
    "function will take value of year as YYYY and check whether year is a leap or non"
    text = leap_year(year) 
    if text == True:
        mon_max = { 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        lp_mon = mon_max
        return lp_mon #dictionary object with leap year month
    else:
        mon_max = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        nlp_mon = mon_max
        return nlp_mon #dictionary object with Non-leap year month

def valid_date(date):
    "This function will check the date"
    "if date is valid it will pass"
    if len(str(date)) != 10:
       return 'wrong date entered'
    else:
        str_day, str_month, str_year = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = str(str_day)
        text = days_in_mon(str(year))
        val = text.get(month)
        if month not in range(1, 13):  
            return 'Error: wrong month entered'
        elif int(day) not in range(1, val):
            return 'Error: wrong day entered'
        else:
            return True
            

def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    if len(today) != 10:
        return 'Error: wrong date entered'
        
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        text = days_in_mon(str(year))
        val = text.get(month) 

        tmp_day = day + 1 # next day
        if tmp_day > val:
            to_day = tmp_day % val # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the previous day in DD-MM-YYYY format."
    if len(today) != 10:
        return 'Error: wrong date entered'
     
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        text = days_in_mon(str(year))
        


        tmp_day = day - 1 # previous day
        if tmp_day < 1:
            tmp_month = month -1
            if tmp_month < 1:
                to_month = 12
                year = year - 1
            else:
                to_month = tmp_month 
            

            val = text.get(to_month)
            to_day = val # if tmp_day < 1, reset to last day of previous month
        else:
            to_day = tmp_day
            to_month = month - 0

        

        previous_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return previous_date
    

def dbda(start_date, num_days):
    "This is our main function which will accept two arguments date and number of days"
    "then work correspond to value of num_days, if its +ve it will use after function"
    "if its -ve it will use before function"
    pos_num = abs(int(num_days))
    end_date = 0
    # create a loop
    while end_date != pos_num:
    # call before() or after() as appropriate
        if int(num_days) > 0:
            after(start_date)
            start_date = after(start_date)
 
        elif int(num_days) <0:
            before(start_date)
            start_date = before(start_date)
            
    # return end_date
        end_date += 1
    new_date = start_date
    return new_date


if __name__ == "__main__":
    # process command line arguments
    start_date = sys.argv[1]
    num_days = sys.argv[2]
    # call dbda()
    print(dbda(start_date, num_days))
    # output the result