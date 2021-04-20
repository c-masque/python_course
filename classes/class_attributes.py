'''class Website:
    def  __init__(self, title):
        self.title = title

# instance attribute example time...

ws = Website('My Awesome Title')
print(ws.title)

ws_two = Website('My Second Title')
print(ws_two.title)
'''

class DifferentWebsite:
    title = 'My Class Title' # a class attribute - contained within class
    bleh = 'blah'

dw = DifferentWebsite()
print(dw.bleh) # prints out class attribute

# instant attribute belongs to the instance of usage
# class attribute belongs to class definition