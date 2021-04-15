'''
g $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
o $$$$$$$$$$$$$$$$$
'''

sales_data = {
    'g' : 20,
    'f' : 7,
    't' : 15,
    'o' : 2
}

#print each iteration pulled from dictionary, * value, then new line

department = list(sales_data.copy())
#print(department)
department_sales = list(sales_data.copy().values())
#print(department_sales)

#for x in department:
#    print(x + ' '), department_sales #I very clearly don't know how loops work
#for value in department_sales:
#    print(value)

'''
def make_money() # fuck this I'm taking too long

for x in department_sales:

'''


#histogram format but needs to convert numbers to $ signs... can use loop
for key, value in sales_data.items():
    print(f"{key}: {'$' *value}")

    #this is just not working

#for value in department_sales:
#   print(value

############### SOLUTION ##################
'''
sales = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12,
}

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')
'''