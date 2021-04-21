numbers = [
    8,
    6,
    5,
    5,
    4,
    2
]

def median_finder(numbers_list):

    sorted_list = sorted(numbers_list)
    sorted_list_length = len(numbers_list)

    if sorted_list_length >= 2:
        del numbers_list[0]
        del numbers_list[-1]
        sorted_list_length -= 1

    num_one = numbers_list[0]
    num_two = numbers_list[-1]
    median = (num_one + num_two) // 2
    return median

print(median_finder(numbers))