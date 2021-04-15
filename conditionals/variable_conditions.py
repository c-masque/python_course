sentence = 'Sphinx of black quartz, judge my vow...'
word = 'sphinx'

if word.lower() in sentence.lower():
    print('The word was found.')
else:
    print('Word was not found.')

## collections of data ##

nums = [ 1, 2, 3, 4]

if 3 in nums:
    print('hell yeah')
else:
    print('hell nah')