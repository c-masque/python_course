"""
#########################################################################################
You have been given a raw data dump that is structured as an array of objects.
The object's keys are companies, and the values are arrays of emails followed by
a 3 digit department number. I need you to write a program that will go through the data,
print the emails for each company and what department number that email belongs to.
"""

'''
The output can be formatted however you like, so long as the data is pulled out of their
respective collections.
Example Output:
Company: Dave's Email: test@test.com Dept: 123 Email: test@test.com Dept: 888
Email: test@test.com Dept: 555 Email: test@test.com Dept: 123

Try saving the sample data in s separate file and importing it into your main project file.
'''

data = [
{ "Google": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 123" ]},
{ "Yahoo": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 451" ]},
{ "IBM": ["test@test.com 888", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "GREGS": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "AUTO SHOP": ["test@test.com 888", "test@test.com 555", "test@test.com 555", "test@test.com 123" ]},
{ "PAWN SHOP": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Nike": ["test@test.com 123", "test@test.com 123", "test@test.com 555", "test@test.com 123" ]},
{ "Franks": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]},
{ "Tims": ["test@test.com 123", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "Apple": ["test@test.com 123", "test@test.com 555", "test@test.com 123", "test@test.com 123" ]},
{ "Sony": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Disney": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "Popies": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Sally": ["test@test.com 123", "test@test.com 555", "test@test.com 888", "test@test.com 123" ]},
{ "Henry": ["test@test.com 123", "test@test.com 555", "test@test.com 555", "test@test.com 555" ]},
{ "Dave's": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]}
]

def data_cleaner(data_dump):
    result = []

    for data_chunk in data_dump:
        for company_data in data_chunk:
            data_chunk_temp = data_chunk.copy()
            company_name = list(data_chunk_temp.keys())[0]
            company_employee_data = list(*data_chunk_temp.values())[0:]
            cleaned_data = '\n' + company_name + ': ' + '| '.join(company_employee_data)
            result.append(cleaned_data)
    return result


print(*data_cleaner(data))

'''
Essay questions:

What is the Zen of Python? - PEP 20, or the 'Zen of Python' goes over the fundamental guidelines of styling/writing Python in the most effective courtesy possible
What purpose does indentation serve in Python? - Similar to semi colons in css, it is a way of nesting related functions/properties and telling your repl to execute the next step
List at least 5 python Data Types. - Integers, strings, floats, dictionaries, tuples...
Are Python Strings immutable or mutable? - Immutable
Are Python Lists immutable or mutable? - Mutable
What can be stored in a Python List? -Any data type can be stored, though it is best to keep the data types the same
Explain what a Python Dictionary is and how you might use one. - An ordered collection with key and value pairs
What is a Tuple in python? - An ordered and immutable type of collection, similar in structure to a list but uses parantheses
What is a Set in python? - Similar in structure to a list or tuple, but unordered, immutable and specifically has no duplicate values; uses curly brackets
What is List Comprehension in Python? - A special way to
What does it meant to return a value from a python method/function? - when the function is called, the returned value is the output and can be printed or whatever you want to do with it
What is a named argument? - An argument within a function with a name assigned to it... So when the function is called, a value can be manually assigned to the named function, regardless of the order.
What does the *args  do in a python function and how might you use it? - A way to include an unspecified number of arguments into a function
What are Keyword Arguments in Python?
'''