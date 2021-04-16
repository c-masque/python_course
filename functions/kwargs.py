def greeting(**kwargs): # unpacking kwargs returns a dictionary
    if kwargs: # this checks if they were set
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print('Hi, have a great day!')

greeting(first_name = 'Maud', last_name = 'Ox')