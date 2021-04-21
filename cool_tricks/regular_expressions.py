# A.K.A. 'a visual representation of the kid who
# tried to convince everyone he could speak in binary back
# # in high school' or 'that doesn't look regular' expressions

import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files:", file)
        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)

#list_files()

websites = [
    'Apple.com',
    'Orange.net',
    'Kiwi.net',
    'Plum.org'
]

net_websites = [
    site for site in websites if fnmatchcase(site, '*.net')
]

print(net_websites)