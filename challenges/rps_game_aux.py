
def make_a_selection():

    weights = {
        'What move would you like to make?..': 1,
        'Choose your weapon...': 1,
        'Pick your battle instrument...': 1,
        'Make a selection...': 3
}

    def randomizer(odds_and_ends):

        results_list = list(odds_and_ends.copy().keys())
        weights_list = list(odds_and_ends.copy().values())

        random_list = random.choices(
            results_list, weights=(weights_list), k=1)

        return random_list
        
    

    selections = {
        'What move would you like to make?..'
        'Choose your weapon...'
        'Pick your battle instrument...'
        'Make a selection...'
    }

    random.choices(
        selections, weights=(weights_list), k=number_of_outputs)
