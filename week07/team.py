"""
Course: CS101
File: team07.py
Author: Brother Comeau

Description:
  This is the code for the weekly team activity.  
  Please work together in groups of 2 to 3.  
  You will not be sumbitting your code for this activity.
  You are free to continue working on this activity after class if you need more time.
"""

"""
Instructions:

- You will be adding code to the following functions.  
- Each of these functions will return True or False.

Here is an example of prompting the user for a value and displaying True
if the value is over 10.  It displays False if it isn't.

    value = int(input('Enter value: '))
    print(value > 10)

"""

# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# isValue100(99)  = False
# isValue100(100) = True
# isValue100(101) = False

def isValue100(value):
    pass

print('isValue100(99)  =', isValue100(99))
print('isValue100(100) =', isValue100(100))
print('isValue100(101) =', isValue100(101))

# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# isValueOver100(100) = False
# isValueOver100(99)  = False
# isValueOver100(101) = True

def isValueOver100(value):
    pass

print()
print('isValueOver100(100) =', isValueOver100(100))
print('isValueOver100(99)  =', isValueOver100(99))
print('isValueOver100(101) =', isValueOver100(101))

# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# isValueLessThanEqual100(100) = True
# isValueLessThanEqual100(99)  = True
# isValueLessThanEqual100(101) = False

def isValueLessThanEqual100(value):
    pass

print()
print('isValueLessThanEqual100(100) =', isValueLessThanEqual100(100))
print('isValueLessThanEqual100(99)  =', isValueLessThanEqual100(99))
print('isValueLessThanEqual100(101) =', isValueLessThanEqual100(101))

# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# isValue100or200(100) = True
# isValue100or200(99)  = False
# isValue100or200(200) = True

def isValue100or200(value):
    pass

print()
print('isValue100or200(100) =', isValue100or200(100))
print('isValue100or200(99)  =', isValue100or200(99))
print('isValue100or200(200) =', isValue100or200(200))

# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# isNotTrue(True)  = False
# isNotTrue(False) = True
# isNotTrue(200)   = False
# isNotTrue(0)     = True

def isNotTrue(value):
    pass

print()
print('isNotTrue(True)  =', isNotTrue(True))
print('isNotTrue(False) =', isNotTrue(False))
print('isNotTrue(200)   =', isNotTrue(200))
print('isNotTrue(0)     =', isNotTrue(0))


# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# areYouHappyAndKnowIt(T, T) = True
# areYouHappyAndKnowIt(F, T) = False
# areYouHappyAndKnowIt(T, F) = False
# areYouHappyAndKnowIt(F, F) = False

def areYouHappyAndKnowIt(happy, knowit):
    pass

print()
print('areYouHappyAndKnowIt(T, T) =', areYouHappyAndKnowIt(True, True))
print('areYouHappyAndKnowIt(F, T) =', areYouHappyAndKnowIt(False, True))
print('areYouHappyAndKnowIt(T, F) =', areYouHappyAndKnowIt(True, False))
print('areYouHappyAndKnowIt(F, F) =', areYouHappyAndKnowIt(False, False))


# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# The output of the print statements after you complete the function should look like:
# eitherAorB('9') = False
# eitherAorB('A') = True
# eitherAorB('B') = True
# eitherAorB('b') = False

def eitherAorB(letter):
    pass

print()
print("eitherAorB('9') =", eitherAorB('9'))
print("eitherAorB('A') =", eitherAorB('A'))
print("eitherAorB('B') =", eitherAorB('B'))
print("eitherAorB('b') =", eitherAorB('b'))


# TODO -> Complete the following function (ie., remove the 'pass' and add your code)
# Remember that "not" will be executed first if you don't use parentheses for (a or b).
# The output of the print statements after you complete the function should look like:
# notAorB('9') = True
# notAorB('A') = False
# notAorB('B') = False
# notAorB('b') = True

def notAorB(letter):
    pass

print()
print("notAorB('9') =", notAorB('9'))
print("notAorB('A') =", notAorB('A'))
print("notAorB('B') =", notAorB('B'))
print("notAorB('b') =", notAorB('b'))

# --------------------------------------------------------------
# Extra - Searching Internet

# Complete these functions and test them by calling them

# --------------------------------------------------------------
# Find how to test if a string has all letters.
# The output of the print statements after you complete the function should look like:
# isTextAllLetters('abc') = True
# isTextAllLetters('99') = False
# isTextAllLetters('abc99') = False

def isTextAllLetters(text):
    pass

print()
print("isTextAllLetters('abc') =", isTextAllLetters('abc'))
print("isTextAllLetters('99') =", isTextAllLetters('99'))
print("isTextAllLetters('abc99') =", isTextAllLetters('abc99'))


# --------------------------------------------------------------
# Find how to test if a string has all digits.
# The output of the print statements after you complete the function should look like:
# isTextAllDigits('abc') = False
# isTextAllDigits('99') = True
# isTextAllDigits('abc99') = False

def isTextAllDigits(text):
    pass

print()
print("isTextAllDigits('abc') =", isTextAllDigits('abc'))
print("isTextAllDigits('99') =", isTextAllDigits('99'))
print("isTextAllDigits('abc99') =", isTextAllDigits('abc99'))


# --------------------------------------------------------------
# Find how to count the occurrences of a letter in a string.
# The output of the print statements after you complete the function should look like:
# numberOfLetters('abc', 'a') = 1
# numberOfLetters('abcabcabc', 'a') = 3
# numberOfLetters('abcabcabc', 'x') = 0

def numberOfLetters(text, letter):
    """Given a string and a letter, return the "count" of letters found in the string.
       For example: numberOfLetters('abc111222abc', 'a') returns 2
    """
    pass

print()
print("numberOfLetters('abc', 'a') =", numberOfLetters('abc', 'a'))
print("numberOfLetters('abcabcabc', 'a') =", numberOfLetters('abcabcabc', 'a'))
print("numberOfLetters('abcabcabc', 'x') =", numberOfLetters('abcabcabc', 'x'))


# --------------------------------------------------------------
# Write code (doesn't have to be a function) to prompt the user for a number and
# have your code indicate if the number is a multiple of 3.
# Your output might look like this:
# 	Enter number: 300
# 	Is 300 a multiple of 3: True


# TODO -> Add your code here


# --------------------------------------------------------------
# Prompt the user for a grade (0 to 100).  Using IF statements,
# display the letter grade. (you can include '-' and '+' if you want)
# Example:
#    > enter grade: 85
#    > you have a B
# Example:
#    > enter grade: 89
#    > you have a B+

# TODO -> Add your code here
