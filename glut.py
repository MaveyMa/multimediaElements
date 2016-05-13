'''
Credit to https://rdmilligan.wordpress.com for helping us create and understand AR in python.
Also for the web calibration packet
'''



import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np
from objloader import *
from glyphfunctions import *



import cv2
#Main program to work
def get_vectors(image, points):
     
    # order points
    points = order_points(points)
 
    # load calibration data
    with np.load('webcam_calibration_ouput.npz') as X:
        mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
   
    # set up criteria, image, points and axis
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    imgp = np.array(points, dtype="float32")
 
    objp = np.array([[0.,0.,0.],[1.,0.,0.],
                        [1.,1.,0.],[0.,1.,0.]], dtype="float32")  
 
    # calculate rotation and translation vectors
    cv2.cornerSubPix(gray,imgp,(11,11),(-1,-1),criteria)
    rvecs, tvecs, _ = cv2.solvePnPRansac(objp, imgp, mtx, dist)
 
    return rvecs, tvecs
#==============================================================================
# glyph table

# match glyph pattern to database record
def match_glyph_pattern(glyph_pattern):
    
    GLYPH_TABLE = [[[[0, 1, 0, 1, 0, 0, 0, 1, 1],[0, 0, 1, 1, 0, 1, 0, 1, 0],[1, 1, 0, 0, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 1, 0, 0]], SHAPE_CONE],[[[1, 0, 0, 0, 1, 0, 1, 0, 1],[0, 0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 0, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0, 0]], SHAPE_SPHERE]]
    glyph_found = False
    glyph_rotation = None
    glyph_name = None
     
    for glyph_record in GLYPH_TABLE:
        for idx, val in enumerate(glyph_record[0]):    
            if glyph_pattern == val:
                glyph_found = True
                glyph_rotation = idx
                glyph_name = glyph_record[1]
                break
        if glyph_found: break
 
    return (glyph_found, glyph_rotation, glyph_name)

#==============================================================================
def detect_glyphs(frame):
    QUADRILATERAL_POINTS = 4
    BLACK_THRESHOLD = 100
    WHITE_THRESHOLD = 155

    glyphs = []

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(gray, 100, 200)

    # Stage 2: Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    contours = contours[:3]

    for contour in contours:
        # stage Shape 
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01*perimeter, True)

        if len(approx) == QUADRILATERAL_POINTS:
            #print len(approx)
            #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
            topdown_quad = get_topdown_quad(gray, approx.reshape(4, 2))


            # Stage 5: Border check
            if topdown_quad[(topdown_quad.shape[0]/100.0)*5, (topdown_quad.shape[1]/100.0)*5] > BLACK_THRESHOLD:
                continue

            # Stage 6: Match glyph pattern
            glyph_pattern = get_glyph_pattern(topdown_quad, BLACK_THRESHOLD, WHITE_THRESHOLD)
            glyph_found, _, glyph_name = match_glyph_pattern(glyph_pattern)

            if glyph_found:
                # Stage 7: Get rotation and translation vectors
                rvecs, tvecs = get_vectors(frame, approx.reshape(4, 2))
                glyphs.append([rvecs, tvecs, glyph_name])
                
                if glyph_found:
                    # Stage 7: Get rotation and translation vectors
                    rvecs, tvecs = get_vectors(frame, approx.reshape(4, 2))
                    glyphs.append([rvecs, tvecs, glyph_name])
 
    return glyphs
#==============================================================================
def position_glyphs(frame):
    glyphs = []
    glyphs = detect_glyphs(frame)

    for glyph in glyphs:
         
        rvecs, tvecs, glyph_name = glyph

        # build view matrix
        rmtx = cv2.Rodrigues(rvecs)[0]

        view_matrix = np.array([[rmtx[0][0],rmtx[0][1],rmtx[0][2],tvecs[0]],
                                [rmtx[1][0],rmtx[1][1],rmtx[1][2],tvecs[1]],
                                [rmtx[2][0],rmtx[2][1],rmtx[2][2],tvecs[2]],
                                [0.0       ,0.0       ,0.0       ,1.0    ]])

        view_matrix = view_matrix * INVERSE_MATRIX

        view_matrix = np.transpose(view_matrix)

        # load view matrix and draw shape
        glPushMatrix()
        glLoadMatrixd(view_matrix)

        '''
        glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 50, -50, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 1.0, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 1.0, 2.0, 1.0))
        '''

        glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 25, -50, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.64, 0.004428, 0.0, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        #glColor3d(0.0,1.0,0.0)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        if glyph_name == SHAPE_CONE:
            glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 25, -50, 0.0))
            glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.0, 1.0))
            glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
            glCallList(cone.gl_list)
            
        elif glyph_name == SHAPE_SPHERE:
            glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 25, -50, 0.0))
            glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.0, 1.0))
            glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
            glCallList(sphere.gl_list)

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glPopMatrix()
    

#==============================================================================
def _draw_background():
        # draw background
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 1.0); glVertex3f( 4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 0.0); glVertex3f( 4.0,  3.0, 0.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-4.0,  3.0, 0.0)
        glEnd()


#==============================================================================
# The display() method does all the work; it has to call the appropriate
# OpenGL functions to actually display something.
def display():
    glClearColor(0,0,0,0)
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    # ... render stuff in here ...
    # It will go to an off-screen frame buffer.
    glLoadIdentity()

    frame, rgb = get_frame()
    rgb = cv2.flip(rgb, 0)
    
    bg_image = cv2.flip(frame, 0)
    bg_image = Image.fromarray(bg_image)     
    ix = bg_image.size[0]
    iy = bg_image.size[1]
    gl_img = pygame.image.frombuffer(rgb.tostring(), rgb.shape[1::-1], "RGBA")
    #texture_surface = pygame.image.load(texture_data).convert_alpha()
    bg_image = pygame.image.tostring(gl_img, "RGBA", True)
    # setting background color to show
    glColor(1.0,1.0,1.0,1)
    glBindTexture(GL_TEXTURE_2D, texture_background)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)    
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, bg_image)
    #glClearColor(0.0, 0.0, 0.0, 0.0)
    # draw background
    glBindTexture(GL_TEXTURE_2D, texture_background)
    glPushMatrix()
    glTranslatef(0.0,0.0,-10.0)
    _draw_background()
    glPopMatrix()

    image = position_glyphs(frame)
    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()

#==============================================================================
def _init_gl(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)#
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(33.7, 1.3, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
     
    # assign shapes
    #cone = OBJ('colorCube.obj')


    # assign texture
    glEnable(GL_TEXTURE_2D)
    texture_background = glGenTextures(1)


#=============================================================================
def get_frame():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow('frame',frame)

    

    return frame, rgb

#=============================================================================


