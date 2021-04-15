post = ('Python Basics', 'Intro Guide To Python', 'Some Cool Python Content')

posty_list = [
    'Cool Tips',
    'Author Notes',
    'Exit'
]

posty_dict = {
    'Hello': 'Is it me',
}

post += ('Extra Details',)

post += (*posty_list,)

print(post)

post += (*posty_dict,)

print(post)

# COLLECTION OBJECTS ARE MUTABLE WITHIN TUPLE - TUPLE POSITIONING ARE IMMUTABLE
# INDEX POSITION IS RELIABLE