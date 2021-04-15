import math

sale_prices = [
    2,
    5,
    7,
    3,
    2
]

def find_median_odd(number_list):
    sorted_list = sorted(number_list)
    list_length_mid = len(number_list) // 2

    return sorted_list[list_length_mid]

print(find_median_odd(sale_prices))