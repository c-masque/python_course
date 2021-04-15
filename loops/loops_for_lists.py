colors = ('red', 'orange', 'yellow',
    'green', 'blue', 'purple')

'''
color_counter = 0

#a for in loop appears
for color in colors:
    print(color)
    color_counter += 1

print(color_counter)

#if you have a collection with a plural name then iterative
#value is the singular version
#for square in squares: <= like so
'''

colors = {
    'primary': 'red',
    'secondary': 'orange',
    'primary': 'yellow',
    'secondary': 'green'
}

for kind, name in colors.items():
# items creates view into dictionary
# we can put in two variables and it's smart enough to
# separate it all out 
    print('Kind:', kind)
    print('Color:', name)

