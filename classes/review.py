class Fish:
    def __init__(self, first_name, last_name = "Smith", skeleton = "bone", eyelids = "false"):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        return "Swims forwards"

    def swim_backwards(self):
        return 'Swims backwards'

class Trout(Fish):
    def eyelids(self):
        return True

bob = Trout('Bob', 'Fishers')

#print(bob.eyelids())

class ClownFish(Fish):
    def live_with_anemmone(self):
        return "The ClownFIsh is coexisting with sea anemone"

casey = ClownFish('Casey')
print(casey.first_name)
print(casey.last_name)
print(casey.eyelids)
print(casey.swim())
# print(casey.live_with_anemone())

class Shark(Fish):
    # override constructor AND swim backwards but will inherit swim
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids="True"):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids  #this does count as polymorphism even with copy

    def swim_backwards(self):
        return "the shark cannot swim backwards... but can sink backwards"


sammy = Shark("Sammy")
print(sammy.first_name + ' ' + sammy.last_name)

class Coral:
    def community(self):
        return "Coral lives in a community."
    
class Anemone:
    def protect_clownfish(self):
        return "The anemone is protecting the clownfish."


class CoralReef(Coral, Anemone):
    pass

great_barrier = CoralReef()
print(great_barrier.community())
print(great_barrier.protect_clownfish())