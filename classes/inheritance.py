# inheritance is a way to make a specialized versions of classes

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi, {self.first_name} {self.last_name}.'

    def active_users(self):
        raise AttributeError('Standard user cannot view active users.')


class AdminUser(User): # add class as inherited properties
    def active_users(self):
        return 'There are 500 active users' # overrides User active_users because it's more explicit


maud = AdminUser('m.oxalis@gmail.com', 'Maudlin', 'Oxalis')

adam = User('a.viray@gmail.com', 'Adam', 'Viray')

print(maud.greeting())
print(maud.active_users())
#print(adam.active_users()) # because Adam doesn't have permissions

print(adam.greeting())
print(adam.active_users())