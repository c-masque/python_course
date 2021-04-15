#using pop try to solve challenge
#the list at the end should only contain Altuve and Correa

baseball_players = ['Altuve', 'Bregman', 'Correa', 'Springer']
last_player = baseball_players.pop()
second_player = baseball_players.pop(1) #apparently you can pop off index

print(last_player, second_player)

print(baseball_players)

#well pop off then