def manually_incrementing_matrix(num):
    next_chunk = []
    matrix_chunk = list(range(num))
    print(matrix_chunk)

    matrix_counter = len(matrix_chunk)
    while matrix_counter > 1:
        next_chunk = []
        for chunk in matrix_chunk:
            new_chunk = chunk + 1
            next_chunk.append(new_chunk)
        print(next_chunk)
        matrix_chunk = next_chunk
        matrix_counter -= 1


# JORDAN EXAMPLE BELOW

#manually_incrementing_matrix(5)

def manual_incrementing_matrix(n):
    # matrix n x n
    matrix = [ [ None for y in range(n) ] for x in range(n) ]

    counter = 0

    for idx, el in enumerate(matrix):
        
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return list(matrix)

#print(manual_incrementing_matrix(5))

def manual_matrix(n):
    matrix = []

    for i in range(n):
        append_list = []

        for j in range(n):
            append_list.append(i + j)

        matrix.append(append_list)
    
    return matrix

def manual_matrix(n):
        return [[i + j for j in range(n)] for i in range(n)]
        
print(manual_matrix(5))

def manual_matrix(grid_area):
    starting_num = 0
    initial_matrix = grid_area
    matrix = []

    while starting_num != initial_matrix:
        matrix.append(list(range(starting_num, grid_area)))
        starting_num += 1
        grid_area += 1

    return matrix

print('Matrix While: ', manual_matrix(5))


def manual_matrix(grid_area):
    matrix = []
    counter = 0

    while counter < grid_area:
        matrix.append([x for x in range(counter, grid_area + counter)])
        counter += 1

    return matrix

print('Matrix While with Comp: ', manual_matrix(5))