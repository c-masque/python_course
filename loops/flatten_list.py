## cute normal way to combine a list ##
'''
li_one = [1, 2, 3]

li_two = [4, 5, 6]

combined = [*li_one, *li_two] # reminder * spreads list

print(combined)
'''

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [*legacy_customers, *new_customers] # nice but not ideal

print(raw_db)

## iteration loop that seamlessly adds legacy to new ##
## works great for data sets so no duplicates! ##

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)

def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for number in numbers:
        number += 1
        result.append(number)
    
    
    print(result)

loop_over_list()