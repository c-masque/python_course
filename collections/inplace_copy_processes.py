#cannot just simply copy variables, can accidentally reassign variables that are assigned to others

tags = ['python', 'development', 'tutorials', 'code']

#Nope
#tags[-1] = 'Programming'
#
#print(tags)

#tags.extend('Programming') #blew the string up into individual character objects
#tags.extend(['Programming']) #perfectly appended list item - does not return value

new_tags = tags + ['Programming'] #simply adding string and list is no, but square bracket make yes

print(new_tags)

print(tags) #separation of variables helps preserve first variable

tags.append #do similar
tags.extend #do similar