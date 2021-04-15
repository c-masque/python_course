'''
************************COMPLETED*********************************
1) Create One String From Any Given Amount of Strings
 EX: 
 combine_strings("the", "dog") => "the dog"
'''

one_string = 'BlueThing'
two_string = 'RedThing'
three_string = 'YellowThing'
four_string = 'Icannotbelievethisworked'

def the_stringinator(middle_man, *string_things): #looked up how to do any number of args

    result = middle_man.join(string_things) #looked up how to properly join tuples
    return result

print('This is what the stringinator can do: ' + the_stringinator(' ', one_string, two_string, three_string, four_string))

'''
************************COMPLETED*********************************
2) Given a list, concatenate the elements and return a string.
 EX: ['h', 'i', 5] => 'hi5' 
'''

#same thing as above but but need to turn list to strings

mysterious_list = [ #all I did was put this in a string
    'this',
    'is',
    'a',
    'very',
    'mysterious',
    'list'
]
#print(mysterious_list[0]) #index testing only on this line

def the_stringinator_twin(middle_dude, string_things):

   result = middle_dude.join(map(str, string_things)) #map is a join assist function that helps map all list items
   return result

print('This is what the stringinator\'s twin can do: ' + the_stringinator_twin(' ', mysterious_list))
#apparently what I did for the first homework exercise works for number two
#kind of offended

'''
***********************COMPLETED**********************************
3) Sort a string and return it in alphabetical order
 EX: "Hi There" => "eeHhirT"
'''

def string_detangler(word):

    new_and_improved = list(word) #sorted does the list and sort function together
    new_and_improved.sort()
    result = ''.join(new_and_improved).strip()
    return result

print("Your new alphabetized string is: " + string_detangler('canteloupe'))

#def string_detangler(word):
#   return "".join(sorted(string, key=lambda x: x.lower())).strip()

'''
************************COMPLETED*********************************
4) Write a program that prints all of the values of a given dictionary
'''
a_normal_dictionary = {
    'meme': 'ape',
    'kitty': 'cat',
    'hot': 'dog',
    'came out of a hat': 'bat'
}

def dicts_out(for_harambe):

    new_list = []
    #new_list = a_normal_dictionary.values() #this still prints dict_values - too raw

    for value in a_normal_dictionary.values(): #values specifically gives values and not keys when specified
        new_list.append(value) #iterables go through each element in order
    return the_stringinator_twin(' ', new_list)

    #result = a_normal_dictionary.values() #this code belongs to raw data output
    #return result #this code belongs to raw data output

print('The dictionary\'s values are: ' + dicts_out(a_normal_dictionary)) #print is part of function so no need to print, function is function that do