heading = 'Python: An Introduction'

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)

#Similar to the delimiter in Excel

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)

#partition is great to use over split to reassign string segments to new variables
#partition gives a tuple, split gives a list
#partition gives you 3 parts [tuple]