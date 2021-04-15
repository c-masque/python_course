## HOW TO AND WHY TO NEST A FUNCTION IN A FUNCTION ##

def greeting(first, last):
    def full_name():
        return f'{first} {last}'

    print(f'Hi {full_name()}!')


greeting('Maudlin', 'Oxalis')

# Nesting functions is great if you don't need the secondary function
# anywhere else in the program