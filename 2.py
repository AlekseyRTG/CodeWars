# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

from numpy import square


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    square = sq ** 0.5
    if square.is_integer():
        square += 1
        square = square ** 2
    else :
        square = -1
    print(square)
    return square

find_next_square(114)