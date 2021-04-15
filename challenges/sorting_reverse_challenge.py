
def reverse_machine(word):

    #forgot how to cast a string to a list
    #then reverse sort
    #reverse_word = word.split()?

    #return list(word)
    return word[::-1] #apparently double colon reverse things? wtf

print(reverse_machine('apple'))

'''
word = 'apple'
reverse_word = word.split()
print(reverse_word)
'''


string = 'abcdefg'

print(string[0::2]) #the step is a way to tell processor to skip - ::

'''EVERYTHING BELOW IS BAD AND DUMB
def word_reverser(word):
    li = []

    for i in word:
        li.insert(0, i)

    return "".join(li)

print(word_reverser('reverse'))

def word_reverser(word):
    li = list(word)

    li.sort(reverse=True) #oops was alphabetized

    return ''.join(li)
    
'''