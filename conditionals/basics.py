## BASIC SYNTAX ##

age = int(input('How old are you? '))

if age < 25:
    print(f'{age}? Sorry, you have to be at least 25 years old to rent a car in 2018.')
elif age >= 100:
    print('What?! You\'re way too old to rent a car to drive.')
else:
    print('Yeah, you can drive a car.')