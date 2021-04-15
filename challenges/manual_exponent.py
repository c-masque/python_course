from funtools import reduce

"""
#version one by j.hudgens
def manual_exponent(num, exp):
    counter = exp - 1 #need to not multiply by one less
    total = num

    while counter > 0:
        total *= num
        counter = counter - 1
    
    return total

print(manual_exponent(3, 4))
"""

#version two by j.hudgens
def manual_exponent(num, exp):    
    computed_list = [num] * exp #can explode a list => [3, 3]
    return (reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))

'''
#non computed version
def some_func(total, element):
    return total * element
    
[1, 2, 3]
'''

#reduce iterates over and keeps a count
#used often in interviews and in code in general