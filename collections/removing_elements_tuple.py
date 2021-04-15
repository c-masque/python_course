post = (
    'Python Basics',
    'Python Basics [bad]',
    'Intro Guide To Python',
    'Intro Guide To Python [bad]',
    'Some Cool Python Content',
    'Some Cool Python Content [bad]',)

post += ('Finally, Some Good F*cking Food',) #TO ADD

#print(post[0::2])

post = post[:-1] #removing elements from the end

##print('Goodbye horses: \n' + str(post))

post = post[1:] #removing first post

##print('Goodbye horses: \n' + str(post))

post = list(post) #the messy way to remove content
del post[0] #the messy way to remove content DOES A CRIME
post = tuple(post)

print('Goodbye horses: \n' + str(post))