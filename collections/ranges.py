tags = ['soda', 'cake', 'orange', 'tutorial']

tag_range = tags[0:2] #second argument isn't included in this list
tag_range_two = tags[1:] #goes all the way to the end => goes right
# tags[:1] goes left

tag_range_three = tags[:-1] #only features everything but the end object
#apparently just a : does 'all elements'

#print(tag_range)
#print(tag_range_two)
#print(tag_range_three)
#
# tags[1::2] skips twice in a list

#ADVANCED TOPICS FOR RANGES

tags = [
    'ramune',
    'pretzel',
    'honey',
    'celery',
    'green pepper jelly',
    'salt'
]

#tag_range = tags[1:-1] #skips first and last objects
#tag_range = tags[:-1:2] #interval example... every two
tag_range = tags[::-1] #how mysterious and familiar... flips list without alphabetizing it
print(tag_range)

tag_range.sort(reverse=True) #you get None if you try and make this equal a variable - sort does not return a value so cannot be assigned a value

print(tag_range)