# ideally repr gives a pretty and raw output

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        heredoc = f'''
        Class Invoice with properties such as:
        Client, which has a value of '{self.client}''
        '''.strip()

    def __repr__(self):
        return f'Invoice <value: client: {self.client}, total: {self.total}>'
        # great for interpreting where something broke along the way

inv = Invoice('Google', 500)
print(repr(inv))

# string is for nice output
# repr is the true raw data of the class - showing values
# different social expectation of what str and repr print about a class