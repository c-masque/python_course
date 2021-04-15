sum_loop_list =  [
    2,
    3,
    1
]


def sum_loop(li):

    counter = 0
    total = 0

    while counter < len(li):
        total += li[counter]
        counter += 1

    return total

print(sum_loop(sum_loop_list))


def sum_loop_two(summy_list):

    counter = 0

    for number in sum_loop_list:
        counter += number

    return counter

print(sum_loop_two(sum_loop_list))

def sum_not_loop(listy):

    result = sum_loop_list[0] + sum_loop_list[1] + sum_loop_list[2]
    return result

print(sum_not_loop(sum_loop_list))

def li_total_reduce(li):
    return reduce(lambda a, b: a + b, li)

print(li_total_reduce(sum_loop_list))