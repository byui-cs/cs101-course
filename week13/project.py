"""
Course: CS101
File: <name of your file>
Project: <project number>
Author: <Your name>

Description:
  <What does your project/program do?>
"""

"""
Instructions:

Write a program that allows a user to load a data file of monthly temperates
and displays a graph/chart of those temperatures.

See project instructions on downloading the data files.

The data file will contain rows of temperatures in the format:

       29, 13

The first value is the month high and the other the month low.

There is a function written for you that handles the graph display.
You need to look at what that function needs and write the code to read the
data file and store the info appropriately so that you can call the function and
pass the correct info into it.


Sample Output:

Enter filename: values.csv
<... the graph pops up on the screen ...>

"""

import matplotlib.pyplot as plt
import csv


def displayCityGraph(filename, highs, lows):
    """
    This function will display a graph of the high and low tempurates of a city.
    Arguments:
       filename - Name of the data file
       highs    - list of monthly high tempurates
       lows     - list of monthly low tempurates
    """

    # Month names for the X-Axis
    monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # plotting the lines
    plt.plot(monthNames, highs, label='Highs', color='r') 
    plt.plot(monthNames, lows, label='Lows', color='b') 
    
    # naming the x axis 
    plt.xlabel('Months') 

    # naming the y axis 
    plt.ylabel('Temperature') 
    
    # giving a title to my graph 
    plt.title('Yearly Temperature for ' + filename) 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show()


# =======================================================================
# TODO - add your project code here

