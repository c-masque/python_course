'''
heading_generator(title, heading_type)

## HOW IT SHOULD WORK ##

heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Hi there', '3')
<h3>Greeting</h3>
'''

new_blog_post = {
    'greeting': 'Learn How To Code Python',
    'header': 2
    }

#print(new_blog_post['greeting'])

def heading_generator(title, header_type):

    if int(header_type) in range(1,7):
        print(f'<h{header_type}>{title}</h{header_type}>')
    else:
        print('Header not valid.')


heading_generator(new_blog_post['greeting'],new_blog_post['header'])