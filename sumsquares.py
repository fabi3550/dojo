#!/usr/bin/python
import sys

class SumSquares(object):

  def __init__(self, value):

      init_square = value**2
      temp_square = init_square

      i = value - 1
      squares = []

      while i > 0:
          temp_square -= i**2

          if (temp_square > 0):
              squares.append(i)
          elif (temp_square == 0):
              # print(temp_square)
              break
          else:
              temp_square += i**2
              i -= 1

          i -= 1

      if (len(squares) > 0):
          print(squares)

if __name__ == "__main__":

    if len(sys.argv) == 2:

        try:
            value = int(sys.argv[1])
            sq = SumSquares(value)
        except ValueError as e:
            print("Wrong input")
