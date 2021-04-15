## default arguments in a function ##

def greeting(name = 'Guest'):
    print(f'Welcome, {name}!')

#greeting()
#greeting('Maud')

# literally just equate the argument to a string

# a common interview question?

def some_function(collection = []):
    collection.append(1)
    print(id(collection)) # evidence default is stored with list
    return collection


print(some_function())

# DO NOT MAKE A LIST YOUR DEFAULT ARGUMENT!

# Other part of program
print(some_function())
# it is going to print the original collection default item
# mutating collection with default variable

# INSTEAD

#add empty list in collection within function