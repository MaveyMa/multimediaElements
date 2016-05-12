
<<<<<<< HEAD
from displayImages import combine
=======
>>>>>>> master
import cv2.cv as cv
import cv2
def getThresholdImage(im):
    newim = cv.CloneImage(im)
    cv.Smooth(newim, newim, cv.CV_BLUR,12) #Remove noise

<<<<<<< HEAD
    imgFile = cv2.imread('vive.jpg')
=======
    imgFile = cv2.imread('resized_lava.jpg')
>>>>>>> master

    hsv=cv.CreateImage(cv.GetSize(im), 8, 3)
    cv.CvtColor(newim, hsv, cv.CV_BGR2HSV) # Convert image to HSV
    imThreshed = cv.CreateImage(cv.GetSize(im), 8, 1)
    #Do the threshold on the hsv image, with the right range for the yellow color
    cv.InRangeS(hsv, cv.Scalar(20, 100, 100), cv.Scalar(30, 255, 255), imThreshed)
    del hsv
    return imThreshed

def getThresholdGreenImage(im):
    newim = cv.CloneImage(im)
    cv.Smooth(newim, newim, cv.CV_BLUR,12) #Remove noise

    imgFile = cv2.imread('vive.jpg')

    hsv=cv.CreateImage(cv.GetSize(im), 8, 3)
    cv.CvtColor(newim, hsv, cv.CV_BGR2HSV) # Convert image to HSV
    imThreshed = cv.CreateImage(cv.GetSize(im), 8, 1)
    #Do the threshold on the hsv image, with the right range for the green color
    cv.InRangeS(hsv, cv.Scalar(60, 100, 100), cv.Scalar(125, 200, 200), imThreshed)
    del hsv
    return imThreshed

def getThresholdBlueImage(im):
    newim = cv.CloneImage(im)
    cv.Smooth(newim, newim, cv.CV_BLUR,12) #Remove noise

    imgFile = cv2.imread('vive.jpg')

    hsv=cv.CreateImage(cv.GetSize(im), 8, 3)
    cv.CvtColor(newim, hsv, cv.CV_BGR2HSV) # Convert image to HSV
    imThreshed = cv.CreateImage(cv.GetSize(im), 8, 1)
    #Do the threshold on the hsv image, with the right range for the blue color
    cv.InRangeS(hsv, cv.Scalar(120, 100, 100), cv.Scalar(125, 200, 200), imThreshed)
    del hsv

    return imThreshed

def getThresholdRedImage(im):
    newim = cv.CloneImage(im)
    cv.Smooth(newim, newim, cv.CV_BLUR,12) #Remove noise

    imgFile = cv2.imread('vive.jpg')

    hsv=cv.CreateImage(cv.GetSize(im), 8, 3)
    cv.CvtColor(newim, hsv, cv.CV_BGR2HSV) # Convert image to HSV
    imThreshed = cv.CreateImage(cv.GetSize(im), 8, 1)
    #Do the threshold on the hsv image, with the right range for the red color
    cv.InRangeS(hsv, cv.Scalar(0, 100, 100), cv.Scalar(0, 200, 200), imThreshed)
    del hsv
    return imThreshed


capture = cv.CaptureFromCAM(0)

cv.NamedWindow("video")
cv.NamedWindow("thresh")

tmp = cv.QueryFrame(capture)
imgScribble = cv.CreateImage(cv.GetSize(tmp), 8, 3) #Image that will contain lines
#yellow
posx = 0
posy = 0
<<<<<<< HEAD
#blue
bposx = 0
bposy = 0
#red
rposx = 0
rposy = 0
#green
gposx = 0
gposy = 0
=======
imgFile = cv2.imread('resized_lava.jpg') #500 x 281
size = (500, 281)
>>>>>>> master

imgFile = cv2.imread('vive.jpg') #500 x 281
size = (500, 281)
element1 = ""
element2 = ""
while True:
    frame = cv.QueryFrame(capture)
    imgBlueTresh = getThresholdBlueImage(frame)
    imgYellowTresh = getThresholdImage(frame) #Apply the threshold function
    imgGreenTresh = getThresholdGreenImage(frame)
    imgRedTresh = getThresholdRedImage(frame)

    moments = cv.Moments(cv.GetMat(imgYellowTresh),1)
    moment10 = cv.GetSpatialMoment(moments, 1, 0)
    moment01 = cv.GetSpatialMoment(moments, 0, 1)
    area = cv.GetCentralMoment(moments, 0, 0) #Get the center

    bmoments = cv.Moments(cv.GetMat(imgBlueTresh),1)
    bmoment10 = cv.GetSpatialMoment(bmoments, 1, 0)
    bmoment01 = cv.GetSpatialMoment(bmoments, 0, 1)
    barea = cv.GetCentralMoment(bmoments, 0, 0) #Get the center

    rmoments = cv.Moments(cv.GetMat(imgRedTresh),1)
    rmoment10 = cv.GetSpatialMoment(rmoments, 1, 0)
    rmoment01 = cv.GetSpatialMoment(rmoments, 0, 1)
    rarea = cv.GetCentralMoment(rmoments, 0, 0) #Get the center

    gmoments = cv.Moments(cv.GetMat(imgGreenTresh),1)
    gmoment10 = cv.GetSpatialMoment(gmoments, 1, 0)
    gmoment01 = cv.GetSpatialMoment(gmoments, 0, 1)
    garea = cv.GetCentralMoment(gmoments, 0, 0) #Get the center

    lastx = posx
    lasty = posy

    blastx = bposx
    blasty = bposy

    rlastx = rposx
    rlasty = rposy

    glastx = gposx
    glasty = gposy


    if area == 0: #yellow
        posx = 0
        posy = 0

    else:
        posx = moment10/area
        posy = moment01/area

    #blue
    if barea == 0:
        bposx = 0
        bposy = 0
    else:
        bposx = bmoment10/barea
        bposy = bmoment01/barea

    #red
    if rarea == 0:
        rposx = 0
        rposy = 0
    else:
        rposx = rmoment10/rarea
        rposy = rmoment01/rarea

    #green
    if garea == 0:
        gposx = 0
        gposy = 0
    else:
        gposx = gmoment10/garea
        gposy = gmoment01/garea


    if lastx > 0 and lasty > 0 and posx > 0 and posy > 0: #Mean we have received coordinates to print
<<<<<<< HEAD
    #if there is a yellow object present
        #cv2.imshow('dst_rt', imgFile)
        element1 = "Air"
    else:
        element1 = ""
    if blastx > 0 and blasty > 0 and bposx > 0 and bposy > 0: #Mean we have received coordinates to print
    #if there is a yellow object present
        #cv2.imshow('dst_rt', imgFile)
        element2 = "Water"
    else:
        element2 = ""

    if rlastx > 0 and rlasty > 0 and rposx > 0 and rposy > 0: #Mean we have received coordinates to print
    #if there is a red object present
        #cv2.imshow('dst_rt', imgFile)
        element2 = "Fire"
    else:
        element2 = ""

    if glastx > 0 and glasty > 0 and gposx > 0 and gposy > 0: #Mean we have received coordinates to print
    #if there is a green object present
        #cv2.imshow('dst_rt', imgFile)
        element2 = "Earth"
    else:
        element2 = ""


    combine(element1, element2)
    print element1
    print element2


        #image will disappear if the color object is not present
        #cv.DestroyWindow('dst_rt')
=======
        #Draw the line

        #When a yellow object is in the frame this image will appear
        cv2.imshow('dst_rt', imgFile)
        x_offset=y_offset=50
        #frame[y_offset:y_offset+size.shape[0], x_offset:x_offset+size.shape[1]] = size
        #cv.Line(imgScribble, (int(posx),int(posy)), (int(lastx),int(lasty)), cv.Scalar(0, 255,255),3,1)
    else:
        cv.DestroyWindow('dst_rt')
>>>>>>> master
    #Add the frame and the line image to see lines on the webcam frame
    cv.Add(frame, imgScribble, frame)

    cv.ShowImage("video", frame)
    #cv.ShowImage("thresh", imgYellowTresh)

    c=cv.WaitKey(1)
    if c==27 or c==1048603: #Break if user enters 'Esc'.
        break
    elif c== 1048690: # 'r' for reset
        cv.Zero(imgScribble)
