colors = ['red', 'orange', 'yellow',
    'green', 'blue', 'purple']

# Continue / Break - super handy conditionals

'''
for color in colors:
    if color == 'blue':
        print(f'the color is {color}')
        continue
    else:
        print(f'{color} is not blue')
'''

# continue / break make sense

for color in colors:
    if color == 'blue':
        print(f'{color} was found at index {colors.index(color)}')
        break;
    print(color)

# break breaks you out of the block