'''
Write a program that prints the numbers from 1 to 100.
But for multiples of 3, print 'fizz' instead of the number and
for the multiples of 5, print 'buzz'... for numbers which are 
multiples of both 3 and 5, print 'fizzbuzz'.

EC:
Even though I said to have 1 to 100 I want the function to be able
to take any kind of maximum number. So you could pass in 20 and
they'll print out 1 to 20 following the same rules outlined above.
Or you could pass in 1000 and you'll print out 1 to 1000 while
still following all of the same rules.
'''

def fizz_buzz_machine(max_num):
    fizzy_range = list(range(1, max_num + 1))
    #print(str(fizzy_range) + "\n")

    for num in fizzy_range:
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 5 ==0:
            print('buzz')
        elif num % 3 == 0:
            print('fizz')
        else:
            print(num)
            

fizz_buzz_machine(20)