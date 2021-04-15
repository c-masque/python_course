"""
*********************** COMPLETED **********************************
#1) I'm just going to stare at W3school's site and do all their python exercises then return...
"""

word = 'circumbilivagination'
print(len(word))


"""
*********************** COMPLETED **********************************
#2) Take list of words and return the longest one:
#EX: ["PHP", "Backend", "Exercises"] => "Exercises"
"""

def long_word_finder(words):

#a loop to count letters in a word and add to dictionary?
#check for largest using > and < ?
#takes list of words and checks each for length
#compares for largest number
#pick largest number
#return word

    #access list items starting from 0
    #words[0]

    longest_word = ''

    for word in words:
        if len(word) >= len(longest_word): #apparently comparing strings directly does not work
            longest_word = word
        #else not needed since not longest

    return longest_word #apparently longest_word is not ok here


print(long_word_finder(["cat", "horse", "octopus", "tarantula", "protographium marcellus"]))


"""
********************* COMPLETED ************************************
3) Swap first and last characters in a string
Ex: "the dog" => "ghe doT"
    "ABCD" => "DBCA"
    "WINDOWS" => "SINDOWW"
"""

#def the_switcheroo(word)

#slice the first and last letter and switch

#first_letter = word[0]
#last_letter = word[:-1]

#word = word.replace(first_letter, last_letter)
#word = word.replace(last_letter, first_letter)

#too messy
#return word

#print(the_switcheroo('the dog'))

#************************REDO*******************************


def the_switcheroo(word):

    word = word[-1] + word[1:-1] + word[0]  #can rearrange any letters as long as one line - don't have to do multiple

    return word


print(the_switcheroo('canteloupe'))


"""
*********************** COMPLETED **********************************
4) Replace all occurrences of the first letter in a string with '$' EXCEPT for the first letter itself.
EX: "racecar" => "raceca$"
    "retrofit" => "ret$ofit"
    "talkative" => "talka$ive"
    "bobby" => "bo$$y"
"""


def only_one_can_remain(word):

    #set variable with first letter
    #focus on replacing everything after first letter with variable
    #var = var.replace("first letter", "$")

    the_one_that_remains = word[0]
    #chunk together in one string - first letter preserved then change slice of rest of word
    word = the_one_that_remains + word[1:].replace(the_one_that_remains, "$")

    return word


print(only_one_can_remain('sassafras'))

#research replace function

