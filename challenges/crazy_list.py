# Extract the following datasets:
# number 123
# the string 'look at me'
# the number 12
# the string 'this can be super confusing'
# the dictionary
# the list from inside the dictionary


crazy_list = [
  123, 40, 20,
  [
    'Hello', 'look at me',
    [
      'Holy cow', 12,
      {
        'key': 'value',
        'crazy': [
          1, 2, 3
        ]
      }
    ]
  ],
  'what the?',
  [
    'this can be super confusing'
  ]
]

crazy_onetwothree = crazy_list[0]
print(crazy_onetwothree)

#crazy_lookatme = crazy_list[3[1]] #TypeError: 'int' object is not subscriptable
crazy_lookatme = crazy_list[3][1]
print(crazy_lookatme)

crazy_twolve = crazy_list[3][2][1]
print(crazy_twolve)

crazy_confusingstring = crazy_list[5][0]
print(crazy_confusingstring)

crazy_dictionary = crazy_list[3][2][2]
print(crazy_dictionary)

crazy_listlist = crazy_list[3][2][2]['crazy'] #how to extract key value pairs
print(crazy_listlist)

the_definition_of_crazy = crazy_dictionary['crazy']
print(the_definition_of_crazy)