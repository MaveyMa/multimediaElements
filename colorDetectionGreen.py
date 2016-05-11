
import cv2.cv as cv
import cv2
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


capture = cv.CaptureFromCAM(0)

cv.NamedWindow("video")
cv.NamedWindow("thresh")

tmp = cv.QueryFrame(capture)
imgScribble = cv.CreateImage(cv.GetSize(tmp), 8, 3) #Image that will contain lines

bposx = 0
bposy = 0
imgFile = cv2.imread('vive.jpg') #500 x 281
size = (500, 281)

while True:
    frame = cv.QueryFrame(capture)

    imgGreenTresh = getThresholdGreenImage(frame) #Apply the threshold function

    bmoments = cv.Moments(cv.GetMat(imgGreenTresh),1)
    bmoment10 = cv.GetSpatialMoment(bmoments, 1, 0)
    bmoment01 = cv.GetSpatialMoment(bmoments, 0, 1)
    barea = cv.GetCentralMoment(bmoments, 0, 0) #Get the center

    blastx = bposx
    blasty = bposy
    if barea == 0:
        bposx = 0
        bposy = 0

    else:
        bposx = bmoment10/barea
        bposy = bmoment01/barea

    if blastx > 0 and blasty > 0 and bposx > 0 and bposy > 0: #Mean we have received coordinates to print
        #Draw the line

        #When a red object is in the frame this image will appear
        cv2.imshow('dst_rt', imgFile)
        x_offset=y_offset=50
        print 'green'
        #frame[y_offset:y_offset+size.shape[0], x_offset:x_offset+size.shape[1]] = size
        #cv.Line(imgScribble, (int(posx),int(posy)), (int(lastx),int(lasty)), cv.Scalar(0, 255,255),3,1)
    else:
        #image will disappear if the color object is not present
        cv.DestroyWindow('dst_rt')
    #Add the frame and the line image to see lines on the webcam frame
    cv.Add(frame, imgScribble, frame)

    cv.ShowImage("video", frame)
    #cv.ShowImage("thresh", imgBlueTresh)

    c=cv.WaitKey(1)
    if c==27 or c==1048603: #Break if user enters 'Esc'.
        break
    elif c== 1048690: # 'r' for reset
        cv.Zero(imgScribble)
