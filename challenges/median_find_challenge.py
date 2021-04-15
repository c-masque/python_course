''' 
Tools:
- math library
- sorted function
- list slicing
- computations
'''

sale_prices = [
    523,
    532,
    32,
    6,
    73,
    23,
    765,
    32,
    1
]

#if loop taking first and last numbers and del
#if unable, assign to median_var

'''
def median_finder(median_hidden_list):

    sorted_list = sorted(median_hidden_list)
    sorted_list_length = len(median_hidden_list)

    while sorted_list_length > 0:
        del median_hidden_list[0]
        del median_hidden_list[-1]
        sorted_list_length -= 1

    sale_prices = median 
    return median

print(median_finder(sale_prices))
'''

#######################################################

sorted_list = sorted(sale_prices)
print(sorted_list)
sorted_list_length = len(sale_prices)
print(sorted_list_length)

while sorted_list_length > 1:
    del sorted_list[0] #gives an IndexError???
        
print(sorted_list)