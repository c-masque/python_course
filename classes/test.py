'''
class Dog:

    def speak(self):
        print('woof')


new_dog = Dog()

new_dog.speak()


## CONSTRUCTOR FUNCTION ##

class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'meow'

    def get_name(self):
        return self.name


cat_one = Cat('tom')

print(cat_one.speak())
print(cat_one.get_name())

cat_two = Cat('jean')

print(cat_two.speak())
print(cat_two.get_name())
'''

class Pet:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age

    @property
    def get_name(self):
        return self.name

    def speak(self):
        return 'I don\'t speak.'

class Dog(Pet):
    age_conversion = 7 # this needs to be instantiated

    @property
    def color(self):
        color = 'brown'

    def speak(self):
        return 'woof'

    def dog_age(self):
        return self.age * Dog.age_conversion


class Cat(Pet):
    @property
    def color(self):
        return 'The cat\'s color is orange.'

    def speak(self):
        return 'meow'

class Fish(Pet):
    color = 'The fish\'s color is white.'

#chosen_animal = Cat('Tom', 99)
#print(chosen_animal.speak())
#
#chosen_phrase = Dog('Doof', 5)
#print(chosen_phrase.get_name)
#
#print(chosen_phrase.dog_age())

cat = Cat('Meowsy', 5)
print(cat.color)

fish = Fish('Bubbles', 125)
print(fish.color)

# can also just add a color attribute