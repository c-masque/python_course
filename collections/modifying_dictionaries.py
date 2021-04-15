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

teams['ospreys'] = ['Dude', 'Guy'] # can just throw it another key value pair
teams['ospreys'].append('Chick')

#rint(teams)
#rint(teams.values()[]) #cannot treat view objects like true lists
player_list = list(players.copy().values()) #using copies help protect data - thread safe
print(player_list)

#using get function

#featured_team = teams['astros'] #special query
featured_team = teams.get('dirtbags', 'No featured team') #first is key you're looking for, second is back up  result - best practice

#print(players.values())[1])
#
#print(featured_team) #how to print key object view
#
#view objects - allow us to peek values and keys - not lists
#queries are run on a thread and it performs the action
#view objects are used to hold the view and information isn't updated immediately

team_groupings = teams.items()

print(list(team_groupings)[1][1][2]) #len can somehow be used on a dictionary view object - list can make indexing available

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

del dishes['eggs'] #deletes dictionary but the object view is still there

print('Here is a static object view of this dictionary: \n' + str(list(keys)))