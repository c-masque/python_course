# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

username = input('What is your username? ')
user_list = {
    'm.oxalis': 'secret',
    'b.frstn': 'secret',
    't.moti': 'secret',
    'k.zzo': 'secret'
}

if username in user_list.keys():
    print(f'Welcome, {username}.')
    password = input('What is the secret password? ')

    if password in user_list.values():
        print('Welcome...')
    else:
        print('Hm, that\'s not correct.')
else:
    print('Wrong email or password.')