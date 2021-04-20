class Invoice: #common convention capitalizes an invoice

    def __init__(self, client, total):
        self._client = client # if you want a value protected, add underscore - child elements can still access the data
        self.__total = total # private is a dunder...

    def formatter(self):
        return f'{self._client} owes: ${self.__total}'

    #now time for a decorator...
    @property
    def client(self):
        return self._client

    @client.setter # helps set client
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self.__total

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.total)

print(google.client)

google.total = 10000

print(google.total)