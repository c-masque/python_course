user_list = {
    'm.oxalis': '*****',
    'b.frstn': 'secret',
    't.moti': 'secret',
    'k.zzo': 'secret'
}

dummy = 'dummy'

username = input('\nWhat is your username? ')
password = input('What is the secret password? ')

if (username in user_list.keys() or dummy == 'dummy') and password in user_list.values():
    print(f'\nWelcome, {username}.')
elif username in user_list.keys():
    resend_code = input('Hm, it looks like there is a problem.\nWant to try and send a reset key? (y/n): ')
else:
    print('Hm, that\'s not correct.')

## 'and' condition makes sure both conditions are met ##
## 'or' condition makes sure at least one condition is met ##

## username and dummy have to return true, (then) OR password ##

logged_in = True 
standard_user = True

if logged_in and not standard_user:
    print('\n:: - :: - You can access the admin dashboard - :: - ::')
else:
    print('\n:: - :: - You can only access the standard dashboard - :: - ::\n\n\t(n) New Post - (f) Find Post - (z) Log Out')

input('\n')