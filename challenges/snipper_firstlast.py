'''
remove first and last elements from a list
'''

html = ['<h1>', 'Some content', '</h1>']

def head_stripper(html_list):
    html_change = html_list.copy()
    html_list.pop(0)
    html_list.pop()
     
    return html_change


print(head_stripper(html))
print(html)

## ALTERNATIVE ##
'''
_, *two, _ = list_to_clean
# holy cow you can expand the items with * and it fills up space

return two
'''