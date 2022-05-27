#
# main.py
#
# This is the main program for the ProcessDataFiles
# project.  Much of this code is superceded by
# code located in the PySimpleGUI project files.
#
# Author:  Dan Ballard
# Date Created:  February 1, 2022
# Date Last Revised: May 12, 2022
#
# This Python script create a splash screen, 80% of display
# screen size, centered, and displaying a GIF image with needed
# info, which dissapears after 5 seconds.  The main program
# then calls the processdatafiles.py module which connects
# with a client program and downloads the client's data by
# calling the readIncomingMsg method.

import tkinter as tk
import PySimpleGUI as sg

from filenaming import getnewfilename
from fileprocessor import readcsvfile, getcsvtimetag, readfirstframe, readcsvframes
from processdatafiles import readIncomingMsg


def displayflashscreen():
    # a little tkinter used to produce the flash screen.
    root = tk.Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.4, height*0.4, width*0.1, height*0.1))

    # take a .jpg picture you like, add text with a program like PhotoFiltre
    #    (free from http://www.photofiltre.com) and save as a .gif image file
    image_file = "nb.gif"
    #assert os.path.exists(image_file)
    #    use tkinter's PhotoImage for .gif files
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=height*0.4, width=width*0.4, bg="white")
    canvas.create_image(width*0.4/2, height*0.4/2, image=image)
    canvas.pack()

    # show the splash screen for 1000 milliseconds then destroy
    root.after(1000, root.destroy)
    root.mainloop()


#  Executable code in main.py starts here.
#  The program to pop us a flashscreen with the company logo
#  is disabled for now because PyInstaller is unable to find
#  the image file with the logo.  When this problem is resolved
#  we will utilize this method.

    # Display opening flash screen showing the NuShores Logo


displayflashscreen()


#  now try a little pySimpleGUI code to provide popups explaining the process
#  of processing incoming files.

sg.popup_ok('FlackTek File Data Storage', 'This program is used to receive FlackTek \
mixer files and store them in the local file system. ' , grab_anywhere=True,)

# Call the data file transfer program here using the method readIncomingMsg().
# When the transfer is complete we
# then popup a new dialog that the file transfer was successful and the old
# mixer file was deleted.

filename = readIncomingMsg()

# TODO:  Change definition below to use with global representations.
input_file = '/Users/danballard/PycharmProjects/ProcessDataFiles/' + filename

print ("the input file is:" + input_file)
#  read the csv file completely to find the data frames contained in it.

header_list = readcsvfile(input_file)
print(header_list)

# read the first dataframe and process it
# this method returns the modified header list
# along with the timetag information used for
# creating output filenames.
# header_list = readfirstframe(input_file, header_list)
print("header list from readcsvfile")
print(header_list)
timetag_list = getcsvtimetag(input_file)
print("timetag_list")
print(timetag_list)
timetag = timetag_list.pop(0)
print ("timetag:")
new_filename = getnewfilename(timetag)
print("new filename")
print(new_filename)
readfirstframe(input_file, header_list, new_filename)

readcsvframes(input_file, header_list, timetag_list)

sg.popup_timed('Your file transfer operation succeeded!')

