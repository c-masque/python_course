## time to turn the iterator into a generator ##
'''
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

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        index = 0

        while True:
            if index < lineup_max:
                yield self.players[index] # yield tells generator exists
            else:
                index = 0
                yield self.players[index] # like the next function

            index += 1

    def __repr__(self):
        return f'<InfiniteLineup({self.players})'

    def __str__(self):
        return f'InfiniteLineup with the players: {self.players}'


full_lineup = InfiniteLineup(astros) # this instantiates the object
astros_lineup = full_lineup.lineup()

print(repr(astros_lineup)) # doesn't show players because not generated yet
print(str(astros_lineup)) # 

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
'''
# yield takes the place of return to a degree
# generator keeps track of local variables

def custom_generator(li):
    i = 0
    yield li[i]

gen_obj = custom_generator(['a', 'b', 'c'])

for i in gen_obj:
    print(i)


# yield is like return and stores the data but continues reading the code
# keeps track of the value of num... you can keep using the generator
# and it runs the functions again with the updated variables from last time
# but the 'next' is the key for all that

list_comp = [x ** 3 for x in [1, 2, 3, 4, 5]]
print(list_comp)

gen_expression = (x ** 3 for x in [1, 2, 3, 4, 5])
print(gen_expression)

print(next(gen_expression))