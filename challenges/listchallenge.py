#create list with 4 kinds of food, then:
#add bagels to end of list
#add peaches to start of list
#add green beans somewhere in the middle
#oops... replace green beans with pinto beans

list_of_food = ['Rice', 'Okra', 'Carrots', 'Salsify']

print(list_of_food)

list_of_food.append('Bagels')
print(list_of_food)
list_of_food.insert(0, 'Peaches')
print(list_of_food)
list_of_food.insert(2, 'Green Beans')
print(list_of_food)
list_of_food[2] = 'Pinto Beans'
print(list_of_food)
print(list_of_food[1][0]) #literally grab first character out of the second object

list_of_food[1][0] - "C" + list_of_food[1][1:] #the only way to "edit" a string is reconstructing