"""
Course: CS101
File: team06.py
Author: Brother Comeau

Description:
  This is the code for the weekly team activity.  
  Please work together in groups of 2 to 3.  
  You will not be sumbitting your code for this activity.
  You are free to continue working on this activity after class if you need more time.
"""

"""
This team activity will be using the Python turtle library.
(https://docs.python.org/3.3/library/turtle.html?highlight=turtle)

We will be drawing simple shapes using the turtle.  You move the turtle
by using these commands(functions):

forward(distance) - move the turtle forward the given distance


right(angle) - turn the direction of the turtle to the right (angle amount)


left(angle) - turn the direction of the turtle to the left (angle amount)


penup() - As the turtle moves, it draws on the screen.  You can "lift" the
          drawing pen so when the turtle moves, it doesn't draw a line.


pendown() - Put the pen down for drawing


goto(x, y) - Move the turtle to a position on the screen.  (0, 0) is the
             center of the window/screen.  If the pen is down, the turtle
             will draw a line as it moves to the given position.

circle(radius) - Draws a circle with the given radius

"""

from turtle import *

# Sample code to draw a square of size 50
# You can comment it out if you don't need it

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

# TODO -> draw a square of size 200



# TODO -> draw a diamond of size 300 (each side of length 300)



# TODO -> draw a rectangle of size 150 x 250



# TODO -> Create the function "drawSquare(size)" that
#       draws a square of the given size.  Test your function
#       with different size values (call the function and send
#       a different value to size).


# TODO -> Create the function "drawSquare(x, y, size)" that
#       draws a square of the given size starting at the
#       given position of (x, y).  Test your function with
#       different values.


# TODO -> Create the function "drawTriangle(x, y, size)" that
#       draws an equilateral triangle of the given size starting at the
#       given position of (x, y).  Test your function with
#       different values.


# TODO -> Create the function "drawCircle(x, y, size)" that
#       draws circle of the given size (radius) starting at the
#       given position of (x, y).  Test your function with
#       different values.


# TODO -> Using the turtle commands and your drawSquare(), drawTriangle()
#         and drawCircle() functions.  Create something on the screen,
#         anything you choose.
