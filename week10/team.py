"""
Course: CS101
File: team10.py
Project: <project number>
Author: <Your name>

Description:
  <Replace this line with what does your project/program do?>
"""

"""
Instructions:

Your project will be implementing a number of functions.  Each function 
displays a different shape.  Your code MUST only use the following functions
that are found in the project code to display anything to the console. (You
may NOT use print statements in the functions you are completing.)

star()      displays a '*' character without the new line
fill()      displays a '#' character without the new line
space()     displays a ' ' character without the new line
newline()   displays a new line

Each function is called in the main code found at the bottom of this 
project file.  Functions contain the sample output that you need to match.

"""
# =========================================================================
# The next four function should not be changed.  They should be used in the
# functions that you complete.
# =========================================================================
def star():
    """ Display a star without the normal new line """
    print('*', end='')

def fill():
    """ Display a fill character without the normal new line """
    print('#', end='')

def space():
    """ Display a space without the normal new line """
    print(' ', end='')

def newline():
    """ Display a new line """
    print()

# =========================================================================
# This is an example function to give you an idea of what the functions
# below it should work like.  Your functions will need to call the
# appropriate functions (defined above) to draw the expected shapes.
# =========================================================================
def sampleSquare(size):
    """ display a square of stars of the given size
        - The example below has size = 6
    ******  
    *    *
    *    *
    *    *
    *    *
    ******
    """
    print('Sample Square of size', size)

    # display the first row of stars
    for i in range(size):
        star()
    newline()

    # display the "middle" rows.  There are (size - 2) of them
    for i in range(size - 2):
        # for each row: star, spaces (size - 2 of them), star, newline
        star()
        for j in range(size - 2):
            space()
        star()
        newline()
    
    # display the last row of stars
    for i in range(size):
        star()
    newline()

# =========================================================================
# The functions below are the ones YOU need to complete.
# Example output is shown for each.
# =========================================================================
def doubleSquare(size):
    """ Display a square with sides that are 2 stars thick 
        - This example has size = 3
    ******   
    ******
    **  **
    **  **
    ******
    ******
    """
    print('Double Square of size', size)
    pass


def halfAndHalf(size):
    """ Display a square that is half filled 
        - This example has size = 6
    ******  
    *  ##*
    *  ##*
    *  ##*
    *  ##*
    ******    
    """
    print('Half and half square of size', size)
    pass


def rightTriangle(size):
    """ Display a right triangle 
        - This example has size = 4
       *  
      **
     ***
    ****
    """
    print('Right triangle of size', size)
    pass


def twoTriangles(size):
    """ Display two triangles 
        - This example has size = 5
    ***** *   
    **** **
    *** ***
    ** ****
    * *****
    """
    print('Two triangles of size', size)
    pass


def hockeyStick(handleLen, bladeLen):
    """ Display a hockey stick where the handle is of length handleLen
        and the blade is of length bladeLen.
        - This example has handleLen = 6, bladeLen = 7

    *
     *            
      *
       *
        *
         *
          *******
    """
    print('Hockey stick of size', handleLen, 'and', bladeLen)
    pass


def squareInSquare(outerSize, innerSize):
    """ Display a small square inside a larger square 
        - This example has outerSize = 10, innerSize = 4
    **********   
    *        *
    *        *
    *  ****  *
    *  ****  *
    *  ****  *
    *  ****  *
    *        *
    *        *
    **********    
    """
    print('Outer and inner square of size', outerSize, 'and', innerSize)
    pass


# =========================================================================
# Main code - Don't change any code below

sampleSquare(4)
sampleSquare(5)

doubleSquare(6)
doubleSquare(9)

halfAndHalf(6)
halfAndHalf(10)

rightTriangle(4)
rightTriangle(6)

twoTriangles(3)
twoTriangles(7)

hockeyStick(4, 2)
hockeyStick(6, 7)

squareInSquare(10, 4)
squareInSquare(12, 6)
