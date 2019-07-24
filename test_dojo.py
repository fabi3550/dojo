#!/usr/bin/python

import random
from sumsquares import SumSquares

for test in range(0, 3000):
    r = random.randint(0, 10000000)
    print("Aufgabe: %i" %(r))
    sq = SumSquares(r)
