from colorDetectionBlue import getThresholdBlueImage
import cv2.cv as cv
import cv2
import maveygravy #IMPORT MAVEY'S PYTHON FILE

def getThresholdImage(im):
    newim = cv.CloneImage(im)
    cv.Smooth(newim, newim, cv.CV_BLUR,12) #Remove noise

    imgFile = cv2.imread('vive.jpg')

    hsv=cv.CreateImage(cv.GetSize(im), 8, 3)
    cv.CvtColor(newim, hsv, cv.CV_BGR2HSV) # Convert image to HSV
    imThreshed = cv.CreateImage(cv.GetSize(im), 8, 1)
    #Do the threshold on the hsv image, with the right range for the yellow color
    cv.InRangeS(hsv, cv.Scalar(20, 100, 100), cv.Scalar(30, 255, 255), imThreshed)
    del hsv
    return imThreshed

capture = cv.CaptureFromCAM(0)

cv.NamedWindow("video")
cv.NamedWindow("thresh")

tmp = cv.QueryFrame(capture)
imgScribble = cv.CreateImage(cv.GetSize(tmp), 8, 3) #Image that will contain lines

posx = 0
posy = 0
bposx = 0
bposy = 0
imgFile = cv2.imread('vive.jpg') #500 x 281
size = (500, 281)
element = ""
while True:
    frame = cv.QueryFrame(capture)
    imgBlueTresh = getThresholdBlueImage(frame)
    imgYellowTresh = getThresholdImage(frame) #Apply the threshold function

    moments = cv.Moments(cv.GetMat(imgYellowTresh),1)
    moment10 = cv.GetSpatialMoment(moments, 1, 0)
    moment01 = cv.GetSpatialMoment(moments, 0, 1)
    area = cv.GetCentralMoment(moments, 0, 0) #Get the center

    bmoments = cv.Moments(cv.GetMat(imgBlueTresh),1)
    bmoment10 = cv.GetSpatialMoment(bmoments, 1, 0)
    bmoment01 = cv.GetSpatialMoment(bmoments, 0, 1)
    barea = cv.GetCentralMoment(bmoments, 0, 0) #Get the center

    lastx = posx #yellow
    lasty = posy
    blastx = bposx #blue
    blasty = bposy
    if area == 0: #yellow
        posx = 0
        posy = 0
    else:
        posx = moment10/area
        posy = moment01/area
    if barea == 0: #blue
        bposx = 0
        bposy = 0

    else:
        bposx = bmoment10/barea
        bposy = bmoment01/barea
    #IF CAMERA SEES YELLOW, IT'S AIR. DISPLAY AIR.
    if lastx > 0 and lasty > 0 and posx > 0 and posy > 0: #Means we have received coordinates to print
        #Draw the line

        #When a yellow object is in the frame this image will appear
        cv2.imshow('dst_rt', imgFile)
        element = "Air"
        print element
        #frame[y_offset:y_offset+size.shape[0], x_offset:x_offset+size.shape[1]] = size
        #cv.Line(imgScribble, (int(posx),int(posy)), (int(lastx),int(lasty)), cv.Scalar(0, 255,255),3,1)
    #IF CAMERA SEES BLUE, IT'S WATER. DISPLAY BLUE.
    elif blastx > 0 and blasty > 0 and bposx > 0 and bposy > 0:
        element = "Water"
        print element
    #TODO:IF CAMERA SEES RED, IT'S FIRE. DISPLAY FIRE.
    #RIGHT NOW THIS IS AN ELSE STATEMENT. BUT TODO: IF CAMERA SEES GREEN, IT'S EARTH. DISPLAY EARTH.
    else:
        element = "Earth"
        print element
        #image will disappear if the color object is not present
        cv.DestroyWindow('dst_rt')
    #Add the frame and the line image to see lines on the webcam frame
    cv.Add(frame, imgScribble, frame)

    cv.ShowImage("video", frame)
    #cv.ShowImage("thresh", imgYellowTresh)

    c=cv.WaitKey(1)
    if c==27 or c==1048603: #Break if user enters 'Esc'.
        break
    elif c== 1048690: # 'r' for reset
        cv.Zero(imgScribble)
