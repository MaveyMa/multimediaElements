
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
