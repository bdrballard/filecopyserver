# globals.py
'''
    This fie contains the global variables used in the
    file processing programs.  This code contains file path
    information which must be updated prior to
    deploying it to the server aphrodite.

    Code Author:  Dan Ballard
    Date Written:  April 2, 2022
    Date Last Updated:  April 23, 2022
'''

def initialize():
    global EQUIPMENT_DESIGNATOR
    global RAW_FILE_PATH
    global RAW_FILE_NAME
    global NEW_FRAME_FILE_PATH
    return

    #EQUIPMENT_DESIGNATOR = 'MTA'
    #RAW_FILE_PATH = '/Users/danballard/Desktop/'
    #RAW_FILE_NAME = '2111190013.csv'
    #NEW_FRAME_FILE_PATH = '/Users/danballard/Desktop/'


def EQUIPMENT_DESIGNATOR():
    return 'FTA'

def NEW_FRAME_FILE_PATH():
    return '/Users/danballard/Desktop/'

def RAW_FILE_NAME():
    return '2111190013.csv'

def RAW_FILE_PATH():
    return '/Users/danballard/Desktop/'