class Averager:
    number_list = [1, 2, 3, 4, 5, 6]

    def average_machine(num_list):
        result = 0
        for num in num_list:
            result += num
        result /= len(num_list)

        return []

        return result

    #print(average_machine(number_list))

    def reducer_averager(num_list):
        from functools import reduce

        result = functools.reduce(lambda result, add: result + add, num_list) / len(num_list)

        return result 

    #print(reducer_averager(number_list))

result = lambda x, y: x + y
print(result(4, 6))

## just for fun
#li = [num for num in range(21) if num % 2 == 0]
#print(li)

li = [num for num in range(5) if num % 2 == 0]
matrix = [[i +j for i in range(5)] for j in range(5)]