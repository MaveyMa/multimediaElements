'''
NAME: Mavey Ma
LAST EDITED: May 7, 2016
DESCRIPTION: Graphical User Interface for Element with three buttons:
[TURN ON COLOR-DETECTION] 
[TURN ON CAMERA] - Webcam turns on.
[EXIT] - Closes window
'''
from Tkinter import *
import Tkinter as tk
import cv2
import tkFont
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import numpy as np

#==========FUNCTION DEFINITIONS==========
def showFrame():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
#==========STYLE SET UP==========
#BOX
master = Tk()
#CREATE A CANVAS w SIZE 800x500
w = Canvas(master, width=600, height=500)
#CONTROL WHERE THINGS ARE LOCATED: EXPAND, FILL, SIDES
w.pack()
#SET FONT
courierFont = tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD)
courierText = tkFont.Font(family="Courier", size=15, weight=tkFont.BOLD)
#WINDOW TITLE
master.title("Elemental Color Chemistry [Augment Reality Cards]")
#WELCOME TEXT
welcome = Label(master, text = "Water, Earth, Fire, Air",
                    font=courierText)
welcome.place(x=0,y=0)
#NOTE: TOP FRAME IS DEFAULT
#BOTTOM LOCATION
bottomFrame = Frame(master)
bottomFrame.pack(side=BOTTOM)
#RIGHT LOCATION
rightFrame = Frame(master)
rightFrame.pack(side=RIGHT)
#LEFT LOCATION
leftFrame = Frame(master)
leftFrame.pack(side=LEFT)
#==========BUTTONS==========
""" TEMPLATE FOR BUTTON PARAMETERS
BUTTON(LOCATION, TEXT, FONT,
       FOREGROUND(COLOR OF TEXT), BACKGROUND,
       HOVERTEXT, HOVERGROUND)
"""

#BUTTON UPLOAD: ALLOWS USER TO SELECT A FILE TO UPLOAD
uploadButton = Button(leftFrame, text="OPEN CAM", font=courierFont, 
                      fg="black", bg="LightGreen",
                      activeforeground="white", activebackground="#00BA37",
                      command=showFrame, width = 12)
uploadButton.pack(side=LEFT)

#BUTTON EXIT: CLOSES WINDOW
resetButton = Button(leftFrame, text="EXIT", font=courierFont,
                     fg="black", bg="pink",
                     activeforeground="white", activebackground="#FF0DF2",
                     command=quit, width = 12)
resetButton.pack(side=LEFT)
#==========PROCESS INPUT HERE==========

#END PROGRAM, RUN IT
mainloop()

"""
import Tkinter as tk

#Creates a window with a quit button that does so when clicked.
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
"""
