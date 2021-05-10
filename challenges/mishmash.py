# 1) Write a program that prints the sum of all number type values in a given dictionary
# EX: {"data_1": 100, "data_2": 150, "data_3": 10, "data_4": 100} => 360
# EX: {"data_1": "shouldn't be able to sum me", "data_2": 150, "data_3": 10, "data_4": "Nope"} => 160

a = {"data_1": 100, "data_2": 150, "data_3": 'cat'}
b = {"data_4": 50, "data_5": 70, "data_6": 'dog'}

def dictAdder(dict):
    res = 0

    for i in dict:
        if type(dict[i]) == int:
            res += dict[i]

    return res


print(dictAdder(a))


def dictionary_total(dictionary):
    return sum([i for i in dictionary.values() if type(i) == int or \
    type(i) == float])

print(dictionary_total(a))

# 2) Write a program that merges two dictionaries
# EX: {"a": 100, "b": 200}, {"x": 300, "y", 200} => {"a": 100, "b": 200, "x": 300, "y": 200}

def dictionary_updater(one, two):
    one |= two
    return one

print(dictionary_updater(a, b))

def merger(one, two):
    res = one.copy()
    dictTwo = two.copy()
    res.update(dictTwo)
    return res

print(merger(a, b))

def dict_merge(one, two):
    return { **one, **two }

print(dict_merge(a,b))


def dict_merge(*dicts):
    new_dict = {}

    for i in dicts:
        for key in i:
            new_dict[key] = i[key]
    
    return new_dict

print(dict_merge(a, b))