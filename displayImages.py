
"""
Augmented Reality Elemental Cards: https://github.com/MaveyMa/multimediaElements
[TEAM 87] Noe Lomeli | Mavey Ma | Mario Martinez | May 13, 2016
[Josh Kling, TA][Spring 2016][Professor Avner Biblarz]
[Final Project] CST 205: Multimedia Design and Programming
Water + Earth == Mud, Clay (1
Water + Fire == Opposites (2
Water + Air == Ice, Frost (3
Earth + Fire == Lava, Magma (4
Earth + Air == Opposites (5
Fire + Air == Lightning, Electricity (6
"""
#DISPLAY IMAGE, RESIZE IMAGE
import cv2.cv as cv
import cv2
import PIL
from PIL import Image
#================================================================
#SUMMARY: Combines two elements.
#PRE-CONDITION: Pass in two strings (Water, Earth, Fire, Air)
#POST-CONDITION: Print out the result of mixing the two elements.
#================================================================
def combine(firstElement, secondElement):
    #Water + Earth == Mud, Clay
    if ((firstElement == "Water" and secondElement == "Earth") or
        (firstElement == "Earth" and secondElement == "Water")):

        imgFile1 = resizePhoto(500, 'mud.jpg')

        imgFile = cv2.imread(imgFile1) #500 x 281

        cv2.imshow('dst_rt', imgFile)

        #displayImage(imgFile1)
        print "Water + Earth == Mud, Clay!"

    #Water + Fire == Opposites
    elif ((firstElement == "Water" and secondElement == "Fire") or
             (firstElement == "Fire" and secondElement == "Water")):

        imgFile1 = resizePhoto(500, 'waterFire.png')
        imgFile = cv2.imread(imgFile1) #500 x 281

        cv2.imshow('dst_rt', imgFile)
        print "Water + Fire == Opposites!"
    #Water + Air == Ice, Frost
    elif ((firstElement == "Water" and secondElement == "Air") or
             (firstElement == "Air" and secondElement == "Water")):

        imgFile1 = resizePhoto(500, 'ice.jpg')
        imgFile = cv2.imread(imgFile1) #500 x 281

        cv2.imshow('dst_rt', imgFile)
        print "Water + Air == Ice, Frost!"
    #Earth + Fire == Lava, Magma
    elif ((firstElement == "Earth" and secondElement == "Fire") or
             (firstElement == "Fire" and secondElement == "Earth")):

        imgFile1 = resizePhoto(500, 'lava.jpg')
        imgFile = cv2.imread(imgFile1) #500 x 281

        cv2.imshow('dst_rt', imgFile)
        print "Earth + Fire == Lava, Magma!"
    #Earth + Air == Opposites
    elif ((firstElement == "Earth" and secondElement == "Air") or
             (firstElement == "Air" and secondElement == "Earth")):

        imgFile1 = resizePhoto(500, 'earthAir.jpg')
        imgFile = cv2.imread(imgFile1) #500 x 281

        cv2.imshow('dst_rt', imgFile)
        print "Earth + Air == Opposites!"


    #Fire + Air == Lightning, Electricity
    elif ((firstElement == "Air" and secondElement == "Fire") or
             (firstElement == "Fire" and secondElement == "Air")):
        imgFile1 = resizePhoto(500, 'lightning.jpg')
        imgFile = cv2.imread(imgFile1) #500 x 281

        cv2.imshow('dst_rt', imgFile)
        print "Air + Fire == Lightning, Electricity!"
    #else:
        #cv.DestroyWindow('dst_rt')
    #None of the above.


#================================================================
#SUMMARY: Display photo in new window.
#PRE-CONDITION: Pass in fileName string.
#POST-CONDITION: Returns True.
#================================================================
def displayImage(fileName):
    #OPEN THE PICTURE, STORE IN photo
    photo = Image.open(fileName)
    #OPENS IMAGE APP AND DISPLAYS PHOTO
    photo.show()
    return True
#================================================================
#
#================================================================
#SUMMARY: Resize photo proportionately.
#PRE-CONDITION: Pass in baseWidth number and fileName string.
#POST-CONDITION: Returns newFileName string of resized photo.
#================================================================
def resizePhoto(baseWidth, fileName):
    photo = Image.open(fileName)
    wPercent = ( baseWidth / float(photo.size[0]) )
    hSize = int( (float(photo.size[1]) * float(wPercent)) )
    photo = photo.resize( (baseWidth, hSize), PIL.Image.ANTIALIAS)
    newfileName = "resized_" + fileName
    photo.save(newfileName)
    return newfileName
#================================================================




"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#THESE ARE TESTS; COMBINE FUNCTION WORKS. YOU CAN DELETE LATER.
awesome = "Earth"
thing = "Water"
combine(awesome, thing)
#combine("Water", "Earth")
#combine("Water", "Fire")
#combine("Water", "Air")
#combine("Earth", "Fire")
#combine("Earth", "Air")
#combine("Fire", "Air")
#THESE ARE TESTS; COMBINE FUNCTION WORKS. YOU CAN DELETE LATER.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
