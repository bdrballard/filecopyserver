'''
 fileprocessor.py

 Code Author:  Dan Ballard
 Code Written:  January 22, 2022
 Code Last Revised:  March 21, 2022


 This is the major file for processing files transferred from
 the Flacktek mixer.
 TODO:  This code includes all of the calling routines for
 setting up and performing fileprocessing.  These routines
 need to be moved from this file to the main.py calling
 all other programs.

'''

import csv
import pandas as pd
import sys
import globals
from filenaming import getnewfilename
from filenaming import convertTime
from filenaming import convertMonth


def foundheader(input_file, record_number):
    print("IN:foundheader")
    # This method returns true if the record_number
    # is a header, otherwise it returns false
    fields = []
    rows = []
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        print (csvreader)
        fields = next(csvreader)
        record_number = record_number +1
        real_date =fields[5]
        real_year =fields[4]
        real_month_day = fields[3]
        recordf =fields[0]
        print("recordf:%s" % recordf)
        print("record number:%s" % record_number)
        if (recordf == 'Machine Sn'):
            return True
        else:
            return False

# TODO this method is not used
def copyrecord(input_file, output_file):
    print("IN:copyrecord")# This method copies the specified row of data
    # from the source csv file to a destination file
    fields = []
    rows = []
    with open(input_file, 'r') as f1, open("/Users/danballard/Desktop/bar.csv", 'a') as f2 :
     #   line = f1.readline() #remove header
        line = f1.readline()
        print(line[2])
        while line[1] != 'Machine Sn':
            f2.write(line)
            line = f1.readline()


# the retrieveheadertimetag method retrieves the first row
# from a .csv file and creates a timetag for that row.

def retrieveheadertimetag(input_file):
    fields = []
    rows = []
    record_number = 0
    file = open(input_file)

    # read the content of the file opened
    with open(input_file, 'r', encoding="latin-1") as f:
        lines = f.readlines()
    for line in lines[1:]:
        words = line.split()
        if words[0] =='Machine':
            mac_end = words[1][0:2]         #sn tag - fixed length = 2 chars
            msn = words[0] + ' ' + mac_end  #'machine sn label'     = 10 chars
            l1 = len(words[1])
            sn = words[1][3:13]             #serial number  Fixed Length - 10 chars
            dow =words[1][14:l1-1]          #day of week  -VARIABLE
            mnth = words[2]                 #month - VARIABLE
            if len(words[3]) == 15:          # single digit dom
                dom = words[3][0:1]         #day of month -VARIABLE
                year = words[3][2:6]        #year
                time = words[3][7:15]       #time
            else:
                dom = words[3][0:2]         # day of month -VARIABLE
                year = words[3][3:7]        # year
                time = words[3][8:16]       # time
            apm = words[4]                  #am or pm
            if(len(dom) == 1):  dom ='0'+dom
            monthnr = convertMonth(mnth)
            mtime = time + ' ' + apm
            miltime = convertTime(mtime)
            datetime = monthnr + dom + year + miltime
            return datetime


# this method returns the time tag information from
# the header that is used to create the new
# csv filename.  The time tag is the header record
# for the frame in the csv file.
#  TODO:  Look at including this method as part of the readcsv
#  method.  There is a duplication of functions here.

def getcsvtimetag(input_file):
    print("IN:getcvstimetag")
    csv_data = csv.reader(open(input_file))
    # header_list will contain the line numbers for
    # the first header row in csv_data file.
    # initializing the titles and rows list
    fields = []
    rows = []
    line_count = 0
    timetag_list = []
    # reading csv file
    with open(input_file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        print("printing the first header row")
        print(fields)  # print the first header row
        # extracting each data row one by one
        for row in csvreader:
            if line_count == 0:
                line_count = line_count + 1
                timetag_list.append(fields)
            else:
                # print(row)
                line_count = line_count + 1
                if row[0] == 'Machine Sn':
                    print("line_number:%d" % line_count)
                    print(row)
                    timetag_list.append(row)


        # get total number of rows
        print("timetag_list follows:")
        print(timetag_list)
        last_row = csvreader.line_num
        #print("$$$$header_list:%s" % header_list)
        #print("last row is:%d" % last_row)
        print("end of getcsvtimetag")
    return timetag_list


# The readcsvfile method reads the complete raw cvs
# file and determines header row locations and time tag
# locations where are stored in lists that can be popped off

def readcsvfile (input_file):
    print("IN:readcsvfile")
    csv_data = csv.reader(open(input_file))

    # header_list will contain the line numbers for
    # the first header row in csv_data file.
    line_count = 0
    header_list = []
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(input_file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)
        print("printing the first header row")
        print(fields)  #print the first header row
        #line_count=line_count + 1
        # extracting each data row one by one

        for row in csvreader:
            if len(row[0]) < 1:print("Empty Row")
            #rows.append(row)
            #print(row)              #print the entire row
            #print(row[0])           #print specified column data in that row
            if line_count == 0:
                #print(f' Column names are {",".join(row)}')
                line_count = line_count + 1
                header_list.append(line_count)
            else:
                #print(row)
                line_count = line_count + 1
                if row[0] == 'Machine Sn':
                    header_list.append(line_count)
                    print("line_number:%d" % line_count)
                    print(row)
                #line_number = line_count + 1
    # get total number of rows

        last_row = csvreader.line_num
        print("$$$$header_list:%s" % header_list)
        print("last row is:%d" % last_row)
        #add last row to the header_list
        header_list.append(last_row)
        print("printing header_list")
        print(header_list)
        print("end of readcsvfile")
    return header_list
# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))

# The readfirstframe method processes the first frame in
# the raw input file.  This is necessary because of the way
# header information is used in the subsequent data frames.

def readfirstframe(input_file, header_list, new_filename):
    print("IN:readfirstframe")
    end_row = header_list[1]
    csv_data = csv.reader(open(input_file))
    line_count = 0
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open('/Users/danballard/Desktop/2111190013.csv', 'r') as csvfile, open(new_filename, 'a') as csvfileout:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        print(fields)  # print the first header row
        csvfileout.write(', '.join(map(str, fields)))
        for row in csvreader:
            if line_count == 0:
                print(f' Column names are {",".join(row)}')
                column_names = ','.join(map(str, row))
                csvfileout.write(column_names)
                csvfileout.write('\n')
                line_count = line_count + 1
            else:
                if line_count < end_row:
                        print(row)
                        csvfileout.write(','.join(map(str, row)))
                        csvfileout.write('\n')
                        line_count = line_count + 1

        # remove first entry in header list we are through with it.
        header_list.pop(0)
        print("end of readfirstframe")
    return header_list


#  The readcsvframes method reads all subsequent frames and processes
#  them to get the correct header information written to the output file.
def readcsvframes (input_file, header_list, timetag_list):
    print("readcsvframes header list:%s" % header_list)
    print("timetag list")
    print(timetag_list)
    # get next start address and end address from the header list
    # if there is only one entry in the header list then this is
    # the last dataframe and the end
    # TODO Test with larger file sets
    while len(header_list) > 0:

        next_timetag = timetag_list.pop(0)
        print("next_timetag")
        print(next_timetag)
        new_filename = getnewfilename(next_timetag)
        print("new filename:%s" % new_filename)

        #TODO Test with larger file sets
        start_row = header_list.pop(0)
        end_row = header_list.pop(0)
        print("start_row:%d" % start_row)
        print("end_row:%d" % end_row)

        #TODO remove blank Nan lines in input file
        input_filename = globals.RAW_FILE_PATH() + globals.RAW_FILE_NAME()
        # Read the csv file
        df = pd.read_csv(input_filename, skiprows=start_row, nrows=end_row-start_row)
        print("printing df")
        print(df)
        # write to the output file
        df.to_csv(new_filename)
    return


def getFrameLabel(inputfilename):
    xtime = retrieveheadertimetag(inputfilename)
    return xtime




