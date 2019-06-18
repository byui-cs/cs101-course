"""
Course: CS101
File: team10.py
Author: <Your name>

Description:
  This is the code for the weekly team activity.  
  Please work together in groups of 2 to 3.  
  You will not be sumbitting your code for this activity.
  You are free to continue working on this activity after class if you need more time.

"""

"""
Instructions:

Your code will be implementing a number of functions.  Each function 
displays a different shape.  Your code MUST only use the following functions
that are found in the given code below to display anything to the console. (You
may NOT use print statements in the functions you are completing.)

star()      displays a '*' character without the new line
fill()      displays a '#' character without the new line
space()     displays a ' ' character without the new line
newline()   displays a new line

Each function should be called in the main code (at the bottom of this 
file) as a result of the user choosing a menu option.  
Functions contain the sample output that you need to match.

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
def sampleSquare():
    """ display a square of stars of the given size
        - The example below has size = 6
    ******  
    *    *
    *    *
    *    *
    *    *
    ******
    """
    size = int(input('Enter the size: '))
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
def doubleSquare():
    """ Display a square with sides that are 2 stars thick 
        - This example has size = 3
    ******   
    ******
    **  **
    **  **
    ******
    ******
    """
    size = int(input('Enter the size: '))
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
    size = int(input('Enter the size: '))
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
    size = int(input('Enter the size: '))
    print('Right triangle of size', size)
    pass



# =========================================================================
# Main code - implement a menu that allows the user to draw any of the
#             shapes you created with the functions above, until they
#             they enter "0" to exit.
#
"""
Example Output:
    Which shape would you like to draw?
    1) Square
    2) Double Square
    3) Half and Half Square
    4) Right Triangle
    Enter a number or 0 to quit: 1
    
    Enter the size: 6
 
    ******  
    *    *
    *    *
    *    *
    *    *
    ******
    
    Which shape would you like to draw?
    1) Square
    2) Double Square
    3) Half and Half Square
    4) Right Triangle
    Enter a number or 0 to quit: 0
    
    Thanks for drawing!

    
"""

