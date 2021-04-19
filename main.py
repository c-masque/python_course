import sys
sys.path.insert(0, './libs')
from helper import greeting as greet

def render():
    print(greet('Maudlin', 'Oxalis'))


render()