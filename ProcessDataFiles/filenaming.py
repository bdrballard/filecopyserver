# filenaming.py
#
# This file contains functions that are used by the Flacktek File
# processing software.

'''
    Code Author:  Dan Ballard
    Date Written:  January 15, 2022
    Date Last Updated:  March 30, 2022

'''

import csv
import globals
import os


# findMonth is a helper method to find the month in the month_and_day string.
def findMonth(month_and_day):
    month_and_day_length = len(month_and_day)
    month = month_and_day[1: month_and_day_length-2]  # leading blank in December
    return month

# The convertMonth method converts the text representation for each
# month into a new numeric value.  This value is used in constructing
# the file name for a mixer data file.
def convertMonth(case):
    if case == 'January':
        return '01'
    elif case == 'February':
        return '02'
    elif case == 'March':
        return '03',
    elif case == 'April':
        return '04',
    elif case == 'May':
        return '05',
    elif case == 'June':
        return '06'
    elif case == 'July':
        return '07'
    elif case == 'August':
        return '08'
    elif case == 'September':
        return '09'
    elif case == 'October':
        return '10'
    elif case == 'November':
        return '11'
    elif case == 'December':
        return '12'
    else:
        return 'error! month entry'

# The convertDay method converts the month_and_date field from the
# file header and returns the day portion of the field
def convertDay(month_and_day):
    month_and_day_length = len(month_and_day)
    day = month_and_day[month_and_day_length - 2: month_and_day_length]
    if day[0] ==' ':
        day ='0' + day[1]
    return day


# the convertTime() method converts the time in the form 11:12:55 PM
# to the form 231255.  That is a 24-hour clock coded time

# TODO:  Simplify this code mess
def convertTime (input_time: object) -> object:
    time_length = len(input_time)
    if input_time[time_length - 2:time_length] == 'AM':
        new_time = input_time[0: time_length - 2]
        new_time = new_time.replace(':', '')
        time_length = len(new_time)
        new_time = new_time[0:time_length-1]
        return new_time
    else:       # then it is PM time so add 12 hours
        new_time = input_time[0: time_length - 2]
        new_time = new_time.replace(':', '')
        int_time = int(new_time)
        int_pm_time = int_time + 120000
        time_length = len(str(int_pm_time))
        output_time = int_pm_time[0:time_length-1]
        return output_time


#  The convertYear method removes the first two characters in the year
def convertYear(input_year):
    year_length = len(input_year)
    new_year = input_year[year_length-2:year_length]
    return new_year

#  The method 'getnewfilename' reads the row information
#  from the header
#  and creates a file name for storing that file.
def getnewfilename(master_header):
    machine_sn = master_header[1]
    day_of_week = master_header[2]
    month_and_day = master_header[3]
    year = master_header[4]
    time = master_header[5]
    print("++raw time:%s" % time)
    print(machine_sn, day_of_week, month_and_day, year, time)
    the_month = findMonth(month_and_day)
    print("++ find the month:%s" % the_month)
    the_year = convertYear(year)
    print("++ the year:%s" % the_year)
    the_month = convertMonth(the_month)
    print("++ convert the month:%s" % the_month)
    the_day = convertDay(month_and_day)
    print("++ converted day:%s" % the_day)
    standard_time = convertTime(time)
    print ("++ converted time: %s" % standard_time)
    new_frame_label = globals.EQUIPMENT_DESIGNATOR() + the_month + the_day + the_year + standard_time
    print("--new frame label:%s" % new_frame_label)
    new_filename = globals.NEW_FRAME_FILE_PATH() + new_frame_label + '.csv'
    return new_filename


