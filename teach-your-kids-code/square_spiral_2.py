import turtle

##--------------------------------------------------
##
## Teach Your Kids to Code
## By: Bryson Payne
## Publisher: No Starch Press
## Pub. Date: April 21, 2015
## Print ISBN-13: 978-1-59327-614-0
##
## Chapter 1
##--------------------------------------------------

limit = 400
angle = 67

## Instantiate Pen part of the turtle package
t = turtle.Pen()

## Loop from 0 to 99
for x in range(200):

	## Move forward by x 
    t.forward(x)

    ## turn 90 degrees to the left
    t.left(angle)


print("Done")