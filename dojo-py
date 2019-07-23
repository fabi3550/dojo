#!/usr/bin/python
import sys
import math

class Codewars_10(object):

    def __init__(self, value):

        # Erstmal Startparameter ausgeben
        print("initial value is %d, square is %d" % (value, value**2))

        # Liste der kleineren Quadrate bilden, also alle unter dem Startparameter
        # Wird spaeter benoetigt fuer die Multiplikation
        lst_squares = [i**2 for i in range(value, 1, -1)]
        # print(lst_squares, len(lst_squares))

        # Entscheidend ist, dass die Liste i-1 gross ist. Das ist die Anzahl der "Bits",
        # die ich spaeter fuer meine Berechnung brauche. Formel 2^i-1
        # Fuer 7 ist das also 2^7-1 = 127 -> groesstdarstellbare Zahl mit 7 bit
        # Daraus ergeben sich 127 moegliche Iterationen an bits, die in der naechsten Schleife
        # ausgegeben werden. Wichtig ist: Die Anzahl der Stellen (7) ist gleich der Listen-
        # laenge

        for x in range(1, 2**len(lst_squares) - 1):
            #print("{:#b}".format(x).split("b")[1])
            print("---")
            z0 = ""
            if len("{:#b}".format(x).split("b")[1]) < len(lst_squares):

                for z in range(0, len(lst_squares) - len("{:#b}".format(x).split("b")[1])):
                    z0 += "0"

            bin_val = z0 + "{:#b}".format(x).split("b")[1]

            u = 0 # billige zaehlvariable
            sum = 0
            for c in bin_val:
                print(bin_val, int(c), u, lst_squares[int(c)])
                sum += int(c) * lst_squares[int(c)]
                u += 1

            print(sum)

if __name__ == "__main__":

    if len(sys.argv) == 2:

        try:
            value = int(sys.argv[1])
            cw = Codewars_10(value)
        except ValueError as e:
            print("Wrong input")
