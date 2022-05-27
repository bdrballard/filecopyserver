'''This is a collection of studies determining how to use the
packages PySimpleGUI and tkinter.

This code is example only and while what was learned here
is useful, this code, as is, is unlikely to be
included in the Flacktek package.  However, it does show
how to use PySimpleGui for our immediate needs.
The tkinter code for displaying a spash screen works but
is not usable until I can figure out how to get the
program PyInstaller to read an image file.  Version 1.0
of our code likely will not include the flash screen.

I will need to create a new main.py for this package because
the current main.py is not usable.
'''

# create a splash screen, 80% of display screen size, centered,
# displaying a GIF image with needed info, disappearing after 5 seconds

import tkinter as tk
import PySimpleGUI as sg
print(sg)
import os

# Display opening flash screen showing the NuShores Logo
# a little tkinter used to produce the flash screen.
root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

# take a .jpg picture you like, add text with a program like PhotoFiltre
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = "nb.gif"
#assert os.path.exists(image_file)
# use tkinter's PhotoImage for .gif files
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="white")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

# show the splash screen for 5000 milliseconds then destroy
root.after(1000, root.destroy)
root.mainloop()

#  The console program can start here ...
#  now try a little pySimpleGUI code to provide popups explaining the program.
#  This codelet will startup the Flacktek Server code and the
#  Flacktek MixerFileManager code.

sg.popup_ok_cancel('FlackTek File Manager', 'This program is used to transfer FlackTek \
mixer files to the main server.  Click OK to move the mixer file to the central \
server and delete it from this machine..', grab_anywhere=True,)

# Call the file transfer program here.  When the transfer is complete
# then popup a new dialog that the file transfer was successful and the old
# mixer file was deleted.
layout = [[sg.Text('Are you sure?')],
          [sg.Text('Click Ok to continue or hit the Cancel button')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window =sg.Window('Continue', layout, enable_close_attempted_event=True)
canceled = 0

while True:
    event, values = window.read()
    print(event, values)

    if(event == 'Ok'): break
    if (event == 'Cancel'): break
    #if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and event == 'Cancel'):
      #  break

window.close()
if event == 'Cancel': print("canceled")
else:print ("processing files")
sg.popup_timed('Your transaction was successfully completed!')