# lambdas are good for wrapping up simple processes
# lambdas return values

full_name = lambda first, last: f'{first} {last}'

# assign variables
# then pass function commands

def greeting(name):
    print(f'Hi there {name}')

greeting(full_name('Maud', 'Ox'))

# can pass through a function with the variables