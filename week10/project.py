"""
Course: CS101
File: <name of your file>
Project: <project number>
Author: <Your name>

Description:
  <Replace this line with what does your project/program do?>
"""

"""
Instructions:

Here is a chart of the different starting day values and how they
map to the days of the week.

Day of the week | Starting day value
====================================
Sunday          |   1
Monday          |   2
Tuesday         |   3
Wednesday       |   4
Thursday        |   5
Friday          |   6
Saturday        |   7

Notes: 

1) when the user enters an invalid value for month or start day
   the program needs to ask the user again for a valid value.

2) Your program will need to calculate the number of days in the month
   that the user entered.  For example, if the user enters the number
   8 for August, your program needs to use 31 for the number of days
   for that month.  You can assume that the year is not a leap year
   and that February has 28 days. 

Sample Output (Try different values for testing your project)

Enter month (1 thru 12): 0
Enter month (1 thru 12): 55
Enter month (1 thru 12): 5
Enter start day (1 thru 7): 0
Enter start day (1 thru 7): 99
Enter start day (1 thru 7): 3

         May
 Su Mo Tu We Th Fr Sa
        1  2  3  4  5
  6  7  8  9 10 11 12
 13 14 15 16 17 18 19
 20 21 22 23 24 25 26
 27 28 29 30 31

"""

# TODO -> Define your functions here (look at the Main code to see what
#         function you should be creating).



# =====================================================================
# Main code - Don't modify anything below
# =====================================================================
month = getMonth()
days = getDaysInMonth(month)
startingDay = getStartingDay()
displayMonth(month, startingDay, days)

