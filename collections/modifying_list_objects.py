'''
User Database Query
'''

users = ['Cloudy', 'Jason', 'Sami'] #a list data structure of list objects

#print(users)

#how to add to lists

users.insert(0, "Maud") #adds element to start of list when set to 0

#print(users)

users.append('Adam') #adds element to end of list

#print(users)

#querying item in list

#print(users[2]) #prints third name in list
#print([users[2]]) #literally prints string with brackets n such

#how to change a name

users[2] = 'River' #renames Ian / reassigns data to a string object
#print(users)

#how to remove list items

users.remove('Sami') #takes an argument of value wanted to be removed - great to use this method to search for a value and remove

#print(users)

popped_user = users.pop() #pop off last user and returns for use - specifically great for temprarily using a list object

print(popped_user)
print(users)
#example: you can go through and loop and pop data from a user list and use that 'one user' var and send emails with no duplicates

del users[0] #affects an indexed position specifically
print(users)