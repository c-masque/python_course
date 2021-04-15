## IT IS TIME TO GET FUNC-Y ##
'''
name = {
    'Maudlin': 'Oxalis'
}

def full_name(first, last):
    result = str(first) + str(last)
    return result

print(list(name.keys()))

print(full_name(name.keys(),full_name(name.values())))


## EXAMPLE OF DYNAMIC FULL NAME FUNCTION ##

def full_name2(first, last):
    print(f'{first} {last}')


#full_name2('Maudlin', 'Oxalis')
'''
## EXAMPLE OF IF ELSE IN FUNCTIONS ##

def auth(email, password):
    if email == 'kristine@hudgens.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not authorized.')


#auth('kristine@hudgens.com', 'secret')

## EXAMPLE OF LOOPS IN FUNCTIONS ##

def hundred(max_value):
    for num in range(1,max_value + 1):
        print(num)

number_request = input('What number do you want repeated?')
hundred(500)