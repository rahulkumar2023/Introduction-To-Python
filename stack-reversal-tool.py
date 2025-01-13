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
