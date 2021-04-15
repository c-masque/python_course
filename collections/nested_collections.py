teams = [
  {
    'Astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'Angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

#print(teams[0])

Angels = teams[1].get('Angels', 'Team not found')

print(list(Angels.values())[1])

#print(teams[1]['Angels']['DH'])