#write a program that turns any number into a negative

import math

#def negator(NumOne):
#    NumOne = 5 #garbage
#    total = 0
#
#    total = math.floor(NumOne)
#
#    return total
#
#print(total)
##print(negator(5))

#NumOne = 5
#total = math.floor(NumOne)
#total = NumOne - (total * 2)
#print(total)

def negator(NumOne):
    total = math.floor(NumOne)
    total = NumOne - (total * 2)

    return total

print(negator(5))