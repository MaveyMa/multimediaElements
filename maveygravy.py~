#SKELETON OF THE ALGORITHM
"""
Water + Earth == Mud, Clay (1
Water + Fire == Opposites (2
Water + Air == Ice, Frost (3
Earth + Fire == Lava, Magma (4
Earth + Air == Opposites (5
Fire + Air == Lightning, Electricity (6
"""
#LATER, NEED TO OPEN WINDOW TO DISPLAY AN IMAGE
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
        #OPEN THE PICTURE, STORE IN mud
        mud = Image.open("mud.jpg")
        #OPENS IMAGE APP AND DISPLAYS PHOTO
        mud.show()
    #Water + Fire == Opposites
    elif ((firstElement == "Water" and secondElement == "Fire") or 
             (firstElement == "Fire" and secondElement == "Water")):
        print "Water + Fire == Opposites!"
        waterFire = Image.open("waterFire.png")
        waterFire.show() 
    #Water + Air == Ice, Frost
    elif ((firstElement == "Water" and secondElement == "Air") or 
             (firstElement == "Air" and secondElement == "Water")):
        print "Water + Air == Ice, Frost!"
        ice = Image.open("ice.jpg")
        ice.show() 
    #Earth + Fire == Lava, Magma
    elif ((firstElement == "Earth" and secondElement == "Fire") or 
             (firstElement == "Fire" and secondElement == "Earth")):
        print "Earth + Fire == Lava, Magma!"
        lava = Image.open("lava.jpg")
        lava.show()
    #Earth + Air == Opposites
    elif ((firstElement == "Earth" and secondElement == "Air") or 
             (firstElement == "Air" and secondElement == "Earth")):
        print "Earth + Air == Opposites!"
        earthAir = Image.open("earthAir.jpg")
        earthAir.show()
    #Fire + Air == Lightning, Electricity
    elif ((firstElement == "Air" and secondElement == "Fire") or 
             (firstElement == "Fire" and secondElement == "Air")):
        print "Air + Fire == Lightning, Electricity!"
        lightning = Image.open("lightning.jpg")
        lightning.show()
    #None of the above.
    else:
        print "Error! Code shouldn't reach here."
        lion = Image.open("lion.jpg")
        lion.show()
    return
#========================================

#combine("Water", "Earth")
#combine("Water", "Fire")
#combine("Water", "Air")
#combine("Earth", "Fire")
#combine("Earth", "Air")
#combine("Fire", "Air")


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
