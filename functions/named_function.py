def full_name(first, last):
    print(f'{first} {last}')

#full_name(first = 'Maudlin', last = 'Oxalis')
# no longer positional arguments, they are named
# can rearrange order

# print(f'{0} {1} {2}'.format(args)) # this may work

def greeting(time_of_day, *args):
    print(f"Good {time_of_day}, {' '.join(args)}")

greeting('morning', 'Maudlin', 'Oxalis', 'AnotherName')

# *args is best practice
# args unpack into tuples