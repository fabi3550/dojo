#!/usr/bin/python
import sys

class SumSquares(object):

  def __init__(self, value):
      self.compose(n)

  def compose(self, n):

      init_square = n**2
      temp_square = init_square

      i = n - 1
      squares = []

      while i > 0:
          temp_square -= i**2

          if (temp_square > 0):
              squares.append(i)
          elif (temp_square == 0):
              break
          else:
              temp_square += i**2
              i -= 1
          i -= 1

           if (len(squares) > 0):
               return_value = squares
           else:
               return_value = None

       return return_value

if __name__ == "__main__":

    if len(sys.argv) == 2:

        try:
            value = int(sys.argv[1])
            sq = SumSquares(value)
        except ValueError as e:
            print("Wrong input")
