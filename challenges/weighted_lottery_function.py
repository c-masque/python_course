import random

''' 
weights = {
    'winning': 1,
    'losing': 1000,
}

weighted_lottery(weights) # need to run it 1000 times and only win once
'''

'''
weights = {
    'winning': 1,
    'break even': 2,
    'losing': 3,
}

weighted_lottery(weights) # should still work with more factors apparently
'''

#output should be a string

weights = {
    'winning': 1,
    'break even': 2,
    'losing': 10,
}

number_of_outputs = 5

def randomizer(odds_and_ends):

    results_list = list(odds_and_ends.copy().keys())
    weights_list = list(odds_and_ends.copy().values()) #weights list works
    #print(results_list)

    random_list = random.choices(
        results_list, weights=(weights_list), k=number_of_outputs)

    return random_list

print(randomizer(weights))

'''
def randomizer():

    #pick up all dictionary values to use
    #run through random choices with parameters

print(randomizer(weights))

#use random.choices(-weights go here-)
'''

'''
############ BEST SOLUTION #############
#import numpy # doesn't work in vcs

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        # loop x times
        for _ in range (weight):
            container_list.append(name) #building a container list

        return np.random.choice(container_list)

other_weights = {
    'winning': 1,
    'breaking even': 2,
    'losing': 3
}

print(weighted_lottery(other_weights))
'''