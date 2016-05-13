
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
import maveygravy

#==========FUNCTION DEFINITIONS==========
#================================================================
#SUMMARY: Opens up the web camera
#PRE-CONDITION: Click the OPEN CAM button
#POST-CONDITION: Click 'q' to quit
#================================================================
def combineColorsAvatarState():
    import colorDetection
'''
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
'''

def bendElementsButton():
    import glut.py
    INVERSE_MATRIX = np.array([[ 1.0, 1.0, 1.0, 1.0],
                                [-1.0,-1.0,-1.0,-1.0],
                                [-1.0,-1.0,-1.0,-1.0],
                                [ 1.0, 1.0, 1.0, 1.0]])


    SHAPE_CONE = "cone"
    SHAPE_SPHERE = "sphere"

    width = 640
    height = 480

    glutInit(sys.argv)


    # Create a double-buffer RGBA window.   (Single-buffering is possible.
    # So is creating an index-mode window.)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | OPENGL | DOUBLEBUF)

    glutInitWindowSize(width, height)
    glutInitWindowPosition(800, 400)

    # Create a window, setting its title
    window_id = glutCreateWindow("OpenGL Glyphs")

    # assign texture
    #glEnable(GL_TEXTURE_2D)


    # assign shapes
    cone = OBJ('redColor.obj')
    sphere = OBJ('mk.obj')

    # Run the GLUT main loop until the user closes the window.
    #glutMainLoop()
    global cap
    cap = cv2.VideoCapture(0)
    texture_background = glGenTextures(1)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    _init_gl(width, height)
    glutMainLoop()

    cap.release()
    cv2.destroyAllWindows()
#==========STYLE SET UP==========
#BOX
master = Tk()
#CREATE A CANVAS w SIZE 800x500
w = Canvas(master, width=690, height=490)
#CONTROL WHERE THINGS ARE LOCATED: EXPAND, FILL, SIDES
w.pack()
#SET FONT
courierButton = tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD)
courierWelcome = tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD)
courierText = tkFont.Font(family="Courier", size=45, weight=tkFont.BOLD)
#WINDOW TITLE
master.title("Color Detection | Motion Tracking | Augment Reality")
#WELCOME TEXT AND COLOR LEGEND
welcomeLine1 = Label(master, text = "Choose  2 elements, [BEND ELEMENTS],",
                     font=courierWelcome, background='RoyalBlue4', fg='white')
welcomeLine2 = Label(master, text = "and yield the [AVATAR STATE]...",
                     font=courierWelcome, background='RoyalBlue4', fg='white')
waterSubtitle = Label(master, text = " Water == Blue ", font=courierText,
                      background='gray11', fg='blue')
earthSubtitle = Label(master, text = " Earth == Green ", font=courierText,
                      background='gray11', fg='green')
fireSubtitle= Label(master, text = " Fire == Red ", font=courierText,
                    background='gray11', fg='red')
airSubtitle = Label(master, text = " Air == Yellow ", font=courierText,
                    background='gray11', fg='yellow')
#COORDINATES FOR WHERE TO PLACE THESE TEXT WITHIN THE BOX
welcomeLine1.place(x=15,y=5)
welcomeLine2.place(x=15,y=36)
waterSubtitle.place(x=15,y=90)
earthSubtitle.place(x=15,y=190)
fireSubtitle.place(x=15,y=290)
airSubtitle.place(x=15,y=390)
#CHANGE UGLY GRAY BACKGROUND TO A PLEASANT BLUE ONE
w.configure(background='RoyalBlue4')
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
#BUTTON BEND ELEMENTS: DISPLAY 3D OJECT ON CARDS (MARIO'S CODE)
bendElementsButton = Button(leftFrame, text="BEND ELEMENTS", font=courierButton,
                      fg="white", bg="SpringGreen4",
                      activeforeground="white", activebackground="#00BA37",
                      command=quit, width = 12)
bendElementsButton.pack(side=LEFT)
#BUTTON COMBINE: COLOR DETECTION CREATES THE OUTPUT RESULT (NOE'S CODE)
combineButton = Button(leftFrame, text="AVATAR STATE", font=courierButton,
                      fg="white", bg="DeepSkyBlue2",
                      activeforeground="white", activebackground="turquoise2",
                      command=combineColorsAvatarState, width = 12)
combineButton.pack(side=LEFT)
#BUTTON EXIT: CLOSES WINDOW
resetButton = Button(rightFrame, text="EXIT", font=courierButton,
                     fg="white", bg="firebrick4",
                     activeforeground="white", activebackground="firebrick1",
                     command=quit, width = 12)
resetButton.pack(side=RIGHT)

#==========PROCESS INPUT HERE==========
#some = "Earth"
#thing = "Fire"
#command=lambda: maveygravy.combine(some,thing)
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
