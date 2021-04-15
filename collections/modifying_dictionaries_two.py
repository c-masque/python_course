teams = {
    'astros': ['Altuve', 'Correa', 'Bregman'],
    'dirtbags': ['Bobby', 'SamIAm', 'Judge Judy\'s alter ego']
}

players = {
    'SS': 'Correa',
    '2b': 'Altuve',
    '3b': 'Bregman',
    'DH': 'Gattis',
    'OF': 'Springer',
}

special_team = teams.pop('astros', 'No team found...') #pop also has a secondary alternative return

#print(teams.get('mets', 'No team found...'))

print(teams)
print(special_team) #only values popped off and stored in value

#pop and lock it
#pop is like get where it gives secondary value and can store data
#del just deletes

#nested collections