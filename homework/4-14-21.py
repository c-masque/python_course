import numpy as np
import random

#*********************************************************
# 1)
# Given a list of integers, create a new list ranged from 0 to 20
# omitting the numbers from the original list.
# EX: [1, 3, 5] => [0, 2, 4, 6, 7, 8, 9, 10.....]

num_set = [1, 3, 5]
num_range = range(0,21)

def num_skipper(number_set, range_set):
    
    new_list = [num for num in range_set if num not in number_set]
    return new_list

#print(num_skipper(num_set,list(num_range)))


#*********************************************************
# 2)
# Write a program that separates each character of a string by a hyphen.
# Each character should accumulate based on the current iteration count.
# The start of each accumulated value should be capitalized. 
# IE:  "abcd" => "A-Bb-Ccc-Dddd"
# "RqaEzTy" => "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

def horrifying_ugly_code_maker(stringy):

    monstrosity = stringy[0].upper()
    counter = 1

    while counter < len(stringy):
       # monstrosity = monstrosity + stringy[counter].upper().join # a better version
        half_monstrosity = ''.join((stringy[counter].upper(),\
           stringy[counter] * counter))
        #print(half_monstrosity)
        monstrosity = '-'.join((monstrosity, half_monstrosity))
        counter += 1
    return monstrosity

print(horrifying_ugly_code_maker('okay'))

#*********************************************************
# 3)
# Write a program that generates a random hexadecimal color value
# Hex values are up to 6 character combinations from the values A-Z and numbers 0-9,
# and prefixed by "#"
# EX. #FFFF54, #1235FH, #000458, etc...

def random_color():
    
    # so now it is like below

    color = [''.join([random.choice('ABCDEF0123456789') for each in range(6)])]
    print('https://rgbcolorcode.com/amp/' + str(color[0]))
    return color[0]

print('#' + random_color())