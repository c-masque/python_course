def greeting(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}")

    if kwargs:
        print('Your tasks for the day are:\n')
        for key, val in kwargs.items():
            print(f"{key} => {val}")
    else:
        pass

greeting('Morning',
         'Maud', 'Oxalis',
         first = 'clean kitchen',
         second = 'coding homework',
         third = 'water plants')