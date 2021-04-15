# https://www.google.com/search?q=python+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags) #putting plus between tags list
query_uri = f'{uri}{formatted_tags}' #reminder of f(unction) and string interpolation

print(query_uri)