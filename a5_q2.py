"""
   CISC-121 2023F

   Name:   Rahul Kumar
   Student Number: 20349877
   Email:  21rk74@queensu.ca
   Date: 2023-30-03

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

from Stack_class import *

# Create a new stack
nstack = Stack()

# Take input from user
n = int(input("How many numbers would you like to enter in the stack? "))

for i in range(n):
    item = int(input('Enter a number: '))
    nstack.push(item)

# Print the original List
print("The stack is:")

for i in nstack:
    print(i)
nstack.reverse()

# Reverse the order of the items in the stack
print("The stack, in reverse order, is:")

for i in nstack:
    print(i)