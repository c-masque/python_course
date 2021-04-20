class Invoice: #common convention capitalizes an invoice

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice ('Google', 100)

print(google.client) # it gives you the client name - get method

google.client = 'Yahoo'

print(google.client) # prints out replaced variable
# 'setter process' by setting class variable


