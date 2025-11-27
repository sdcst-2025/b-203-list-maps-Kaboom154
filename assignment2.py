"""
### Assignment 2
Prime numbers
Given a list of numbers that are integers, create a map() that shows whether each of the numbers is a perfect square.
"""

data = [76, 56, 20, 77, 42, 97, 83, 47]

def perfSquare(i):
    root = i ** (1/2)
    if int(root) == root:
        return True
    else:
        return False

squares = map(perfSquare,data)
print(list(squares))

# expected output:  [False, False, False, False, False, True, False, False]
#                                                        ^ this is saying that 97 is a perfect square
