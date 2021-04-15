## IF ELSE FUN! ##

role = 'admin'
auth = 'can access' if role == 'admin' else 'cannot access'

print(auth) # user can now access system because role is 'admin'!

## how to turn off access ##

role = 'guest'

if role == 'admin':
    auth = 'can access'
else:
     auth = 'cannot access'

print(auth)

# can no longer access because a 'guest'... 

# typically it is best to structure edge cases at top of conditional
# tree because it prunes edge cases and gets to the general idea
# else can then cover the general condition