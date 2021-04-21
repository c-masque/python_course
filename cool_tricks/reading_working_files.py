def get_file_contents(filename):
    queried_file = open('cool_tricks\something.txt', 'r')

    if queried_file.mode == 'r':
        return queried_file.read()

    queried_file.close()

content = get_file_contents('cool_tricks\something.txt')

print(content)

print('Number of words', len(content.split()))

print('\n')