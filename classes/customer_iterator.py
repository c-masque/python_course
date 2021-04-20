# we want to build our own iterator through the list... 
# a for loop does work, right? well what if we want it to loop through the
# list entirely and then start back up again on top?


class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1) # the counter

    def __iter__(self): # dunder iter function
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index: # move to the next player
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index: # reset counter
            player = self.get_player(self.n)
            self.n = 0
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros) # OBJECT
process = iter(astros_lineup) # ITERATOR OBJECT

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))

# below is an interator object, not an interable... the interable is each player

#astros_lineup = Lineup(astros)
#process = iter(astros_lineup)

#print(next(process))
# pretend this is like pressing a button it goes to the next dude
