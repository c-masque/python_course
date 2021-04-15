users = ['Cloudy', 'Jason', 'Sami', 'Adam']

IDs = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'apple', users] #different kinds of data - not a good practice

print(mixed_list) #can store list within a list

users_list = mixed_list.pop() #popped off user list

print(users_list) #now can mess around with the popped off list
#storing collections within a list later on... like files

nested_lists = [[123], [234], [345]] #keep things uniform

#example of how clean data is good
li - [[a], [b], [c], 12]

for i in li:
        print(i.upper()) #this doesn't work!

