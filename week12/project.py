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

Write a program that allows a user to create and use a shopping list.  Your
program will display a menu of options to the user.  The user is free
to select any option from the menu in any order.


Sample Output:

Welcome to the shopping list program.

Menu
   n - New shopping list item
   d - Display shopping list
   e - Edit an item in the list
   c - Check or remove item from list
   ? - Display this menu
   q - Quit program
> n
Enter shopping item: Bread
> n
Enter shopping item: Milk
> n
Enter shopping item: Eggs
> d
********* Shopping list *********
* 1  Bread                      *
* 2  Milk                       *
* 3  Eggs                       *
*********************************
> e
Which item do you want to change?: 2
Enter your change: Whole Milk
> d
********* Shopping list *********
* 1  Bread                      *
* 2  Whole Milk                 *
* 3  Eggs                       *
*********************************
> e
Which item do you want to change?: 10
Error: There is no item at that position
> e
Which item do you want to change?: 0
Error: There is no item at that position
> ?
Menu
   n - New shopping list item
   d - Display shopping list
   e - Edit an item in the list
   c - Check or remove item from list
   ? - Display this menu
   q - Quit program
> c
Which item do you want to check?: 10
Error: There is no item at that position
> c
Which item do you want to check?: 1
Item 1 was checked and removed
> d
********* Shopping list *********
* 1  Whole Milk                 *
* 2  Eggs                       *
*********************************
> n
Enter shopping item: Ice Cream
> d
********* Shopping list *********
* 1  Whole Milk                 *
* 2  Eggs                       *
* 3  Ice Cream                  *
*********************************
> q
Good bye

"""

# TODO - add your project code here
