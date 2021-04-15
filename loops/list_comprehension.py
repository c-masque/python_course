## List Comprehension - IT IS HARD ! ##
## set of for loops and conditions that can be ##
## set in a single line of code ##

num_list =range(1, 11) # range creates intergeres from 1 to 11

# we want to cube the numbers in num_list
cubed_nums = []

# traditional way of doing this without list comprehension

for num in num_list:
    cubed_nums.append(num ** 3)

#for comparison
#print(list(num_list))
#print(cubed_nums)

# looks good right? But let's do a list comprehension to make it
# D Y N A M I C

cubed_nums = [num ** 3 for num in num_list] # first action we want to place in this list

print(list(num_list))
print(cubed_nums)

# BAM! A great way to replace for in loops doing basic math
# It generates a new list

## How It Works ##
# The num in the LC has to be identical
# the for loop expression is apparent
# the third key component is the bracket - 
# it tells python the for loop applies to
# dynamically creating a list

# NOW - LET'S ADD A CONDITION!
# we want a list that will capture even numbers...
# let's have a simple loop drawn out first

even_numbers = [] # empty list is important

for num in num_list:
    if num % 2 == 0: # an excellent way to check for even
        even_numbers.append(num)

print(even_numbers)

# now for the list of LC

even_numbers = [num for num in num_list if num % 2 == 0]

# first element is the 'num for' - no need to append
# whatever value we are returning is presumed to add to list
# that's something python does
# BUT only will add the num with the for and if conditional being met


###### TRY IT OUT ######

color_bag = ['red', 'yellow', 'blue']

new_colors = []

for color in color_bag:
    if len(color) > 3:
        new_colors.append(color)

print(new_colors)

color_bag = [color for color in color_bag if len(color) > 3]

print(new_colors)

# you can't make two lists in this LC