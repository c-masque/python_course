import operator
from functools import reduce

def dynamic_reducer(collection, op):
        operators = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv
        }

        return reduce((lambda total, element: operators[op](total, element)), collection)

'''
#print(dynamic_reducer([1, 2, 3], '+'))
#print(dynamic_reducer([1, 2, 3], '-'))
#print(dynamic_reducer([1, 2, 3], '*'))
#print(dynamic_reducer([1, 2, 3], '/'))
#print("***")
#
#def my_reduce(func, collection):
#    total - collection[0]
#
#    for i in collection[1:]:
#        total = func(total, i)
#
#        return totaly

Today:
    Defined a dictionary
    imported dictionaries
    used reduce fuction from dictionary
    learned how to apply variables
    '''