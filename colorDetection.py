
import cv2.cv as cv
import cv2
def getThresholdImage(im):
    newim = cv.CloneImage(im)
    cv.Smooth(newim, newim, cv.CV_BLUR,12) #Remove noise

    imgFile = cv2.imread('resized_lava.jpg')

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
imgFile = cv2.imread('resized_lava.jpg') #500 x 281
size = (500, 281)

while True:
    frame = cv.QueryFrame(capture)

    imgYellowTresh = getThresholdImage(frame) #Apply the threshold function

    moments = cv.Moments(cv.GetMat(imgYellowTresh),1)
    moment10 = cv.GetSpatialMoment(moments, 1, 0)
    moment01 = cv.GetSpatialMoment(moments, 0, 1)
    area = cv.GetCentralMoment(moments, 0, 0) #Get the center

    lastx = posx
    lasty = posy
    if area == 0:
        posx = 0
        posy = 0

    else:
        posx = moment10/area
        posy = moment01/area

    if lastx > 0 and lasty > 0 and posx > 0 and posy > 0: #Mean we have received coordinates to print
        #Draw the line

        #When a yellow object is in the frame this image will appear
        cv2.imshow('dst_rt', imgFile)
        x_offset=y_offset=50
        #frame[y_offset:y_offset+size.shape[0], x_offset:x_offset+size.shape[1]] = size
        #cv.Line(imgScribble, (int(posx),int(posy)), (int(lastx),int(lasty)), cv.Scalar(0, 255,255),3,1)
    else:
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
