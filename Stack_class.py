"""
   CISC-121 2023F

   Name:   Rahul Kumar
   Student Number: 20349877
   Email:  21rk74@queensu.ca
   Date: 2023-30-03

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

class Stack:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """

        self._items = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        empty = False

        if len(self._items) == 0:
            empty = True

        return empty

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
        value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """

        self._items.append(value)

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """

        assert len(self._values) > 0, "Cannot pop an empty stack"
        value = self._items.pop()
        return value  # Otherwise, remove and return the top item from the stack

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """

        assert len(self._values) > 0, "Cannot peek at an empty stack"
        value = self._items[-1]
        return value  # Otherwise, return the top item from the stack (without removing it)

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # Calls the _reverse_aux function on all values within the stack
        self._reverse_aux(0, len(self._items) - 1)

        return

    def _reverse_aux(self, m, n):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        if n > m:
            temp = self._items[m]
            self._items[m] = self._items[n]
            self._items[n] = temp
            self._reverse_aux(m + 1, n - 1)

        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for value in stack:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """

        # The for loop iterates through each value within the stack
        for value in self._items[::-1]:
            yield value

    def reverse(self):
        """
        -------------------------------------------------------=
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # The reverse_r function is called in order to reverse all values within the stack.
        self.reverse_r()
