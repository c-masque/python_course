class Html:
    def __init__(self, content):
        self.content = content 

    def render(self):
        raise NotImplementedError('Subclass must implement render method')


class Heading(Html):
    def render(self):
        return f'<h1>{self.content.title()}</h1>'


class Div(Html):
    def render(self):
        self.content
        return f'<div>{self.content}</div>'


tags = [
        Div('This is some content.'),
        Heading('Some big heading'),
        Div('Another div.')
]

for tag in tags:
    print(tag.render())