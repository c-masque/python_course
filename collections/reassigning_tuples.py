post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))

post += ('seriously',) #always have to have a comma when adding to tuple

print(id(post)) #evidence of new object in memory - tuples are immutable

#title, sub_heading, content, status = post
#
#print(status)

my_list = ['a', 'b', 'c']
my_tup = ('a', 'b', 'c')

my_tup += (*my_list), #CAN EXPAND LIST AND JOIN TO TUPLE

print (my_tup)

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

dictionary = {
    'd': 4,
    'e': 5,
    **dictionary #EXPANDS VALUES TOO
}
