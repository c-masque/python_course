#merge our lists into set of tuples
'''
my_list = ['a', 'b', 'c']
my_tup = ('a', 'b', 'c')

my_tup +=
'''

#the sorted order of your list is important for zip
position = ['2b', '3b', 's', 'dh'] 
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(position, players)

print(list(scoreboard)) #you get a zip object until it is cast to a list

#bam, a tuple