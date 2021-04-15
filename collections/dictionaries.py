#a key value data store

players = {
    'SS': 'Correa',
    '2b': 'Altuve',
    '3b': 'Bregman',
    'DH': 'Gattis',
    'OF': 'Springer',
}

second_base = players ['2b'] #if key doesn't exist, runs KeyError
third_base = players ['3b']

#print(second_base) #pass in key to get to value
#print(third_base)

#guide to nested collections in dictionaries
#can store functions in a dictionary... 


teams = {
    'astros': ['Altuve', 'Correa', 'Bregman'],
    'dirtbags': ['Bobby', 'SamIAm', 'Judge Judy\'s alter ego']
}

print(teams['dirtbags'][-1:])