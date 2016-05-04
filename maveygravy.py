#SKELETON OF THE ALGORITHM
"""
Water + Earth == Mud, Clay (1
Water + Fire == Opposites (2
Water + Air == Ice, Frost (3
Earth + Fire == Lava, Magma (4
Earth + Air == Opposites (5
Fire + Air == Lightning, Electricity (6
"""
#DISPLAY IMAGE, RESIZE IMAGE
import PIL
from PIL import Image 
#========================================
#SUMMARY: Combines two elements.
#PRE-CONDITION: Pass in two strings
#               (Water, Earth, Fire, Air)
#POST-CONDITION: Print out the result of
#                mixing the two elements.
#========================================
def combine(firstElement, secondElement):
    #Water + Earth == Mud, Clay
    if ((firstElement == "Water" and secondElement == "Earth") or 
        (firstElement == "Earth" and secondElement == "Water")):
        print "Water + Earth == Mud, Clay!"
        displayImage(resizePhoto(500, "mud.jpg"))
    #Water + Fire == Opposites
    elif ((firstElement == "Water" and secondElement == "Fire") or 
             (firstElement == "Fire" and secondElement == "Water")):
        print "Water + Fire == Opposites!"
        displayImage(resizePhoto(500, "waterFire.png"))
    #Water + Air == Ice, Frost
    elif ((firstElement == "Water" and secondElement == "Air") or 
             (firstElement == "Air" and secondElement == "Water")):
        print "Water + Air == Ice, Frost!"
        displayImage(resizePhoto(500, "ice.jpg"))
    #Earth + Fire == Lava, Magma
    elif ((firstElement == "Earth" and secondElement == "Fire") or 
             (firstElement == "Fire" and secondElement == "Earth")):
        print "Earth + Fire == Lava, Magma!"
        displayImage(resizePhoto(500, "lava.jpg"))
    #Earth + Air == Opposites
    elif ((firstElement == "Earth" and secondElement == "Air") or 
             (firstElement == "Air" and secondElement == "Earth")):
        print "Earth + Air == Opposites!"
        displayImage(resizePhoto(500, "earthAir.jpg"))
    #Fire + Air == Lightning, Electricity
    elif ((firstElement == "Air" and secondElement == "Fire") or 
             (firstElement == "Fire" and secondElement == "Air")):
        print "Air + Fire == Lightning, Electricity!"
        displayImage(resizePhoto(400, "lightning.jpg"))
    #None of the above.
    else:
        print "Error! Code shouldn't reach here."
        displayImage(resizePhoto(500, "lion.jpg"))
    return
#========================================
def displayImage(fileName):
    #OPEN THE PICTURE, STORE IN photo
    photo = Image.open(fileName)
    #OPENS IMAGE APP AND DISPLAYS PHOTO
    photo.show()
    return True;

def resizePhoto(baseWidth, fileName):
    photo = Image.open(fileName)
    wPercent = ( baseWidth / float(photo.size[0]) )
    hSize = int( (float(photo.size[1]) * float(wPercent)) )
    photo = photo.resize( (baseWidth, hSize), PIL.Image.ANTIALIAS)
    newfileName = "resized_" + fileName
    photo.save(newfileName)
    return newfileName

"""
lion = Image.open("lion.jpg")
wPercent = ( baseWidth / float(lion.size[0]) )
hSize = int( (float(lion.size[1]) * float(wPercent)) )
lion = lion.resize( (baseWidth, hSize), PIL.Image.ANTIALIAS)
lion.save("resizedLion.jpg")
displayImage("resizedLion.jpg")
displayImage(resizePhoto(500, "lion.jpg"))
"""






#combine("Water", "Earth")
#combine("Water", "Fire")
#combine("Water", "Air")
#combine("Earth", "Fire")
#combine("Earth", "Air")
combine("Fire", "Air")


"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#THESE ARE TESTS; COMBINE FUNCTION WORKS. YOU CAN DELETE LATER.
awesome = "Earth"
thing = "Water"
combine(awesome, thing)
combine("Water", "Earth")
combine("Water", "Fire")
combine("Water", "Air")
combine("Earth", "Fire")
combine("Earth", "Air")
combine("Fire", "Air")
#THESE ARE TESTS; COMBINE FUNCTION WORKS. YOU CAN DELETE LATER.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print "MAVEY GRAVY TESTING"
