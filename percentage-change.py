"""
This is a function that takes two arguments
'initialValue && laterValue' and calculates the
diffrence in percentage.

A use-case would be to take in 2 values 
(that are recording from the same source) one by one over
some time, then be returned the percentage 'change()' of
the source.
"""

import numpy




initialValue = 2
laterValue = 5
#inital = a, update = b

def change(a,b):
    #solution unrounded for more accurate calculations
    global solRaw
    #solution rounded for easier display to user
    global solRound
    #sol = SOLUTION
    sol = ((b-a)/a)*100
    solRaw = sol
    solRound = numpy.around(sol, decimals=3)
    print("The value has changed by " + str(solRound)  +"%")


change(initialValue , laterValue)

exit()