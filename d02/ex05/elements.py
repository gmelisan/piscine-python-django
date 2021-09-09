from elem import *

class Html(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'html', attr, content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'head', attr, content) 

class Body(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'body', attr, content) 

class Title(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'title', attr, content) 

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'meta', attr, content, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'img', attr, content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'table', attr, content) 

class Th(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'th', attr, content) 

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'tr', attr, content) 

class Td(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'td', attr, content) 

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'ul', attr, content) 

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'ol', attr, content) 

class Li(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'li', attr, content) 

class H1(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'h1', attr, content) 

class H2(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'h2', attr, content) 

class P(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'p', attr, content) 

class Div(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'div', attr, content) 

class Span(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'span', attr, content) 

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'hr', attr, content, tag_type='simple') 

class Br(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, 'br', attr, content, tag_type='simple') 

def test():
    print(
        Html([
            Head([
                Title(Text('“Hello ground!”')),
                Meta(attr={'charset': 'utf-8'})
            ]),
            
            Body([
                H2(Text('Header 2')),
                Hr(),
                P(Text('Lorem ipsum')),
                Table([
                    Tr([Th(Text('1')), Th(Text('2'))]),
                    Tr([Td(Text('3')), Td(Text('4'))])
                ]),
                Ul([
                    Li(Text('ol1')),
                    Li(Text('ol2'))
                ]),
                Ol([
                    Li(Text('ol1')),
                    Li(Text('ol2'))
                ]),
                Div(Text('text in div')),
                Br(),
                Br(),
                Span(Text('text in span')),
            ])
        ])
    )
    print('---------------')
    print( Html( [Head(), Body()] ) )
    print('---------------')
    print(
        Html([
            Head(
                Title(Text('“Hello ground!”'))
            ),
            Body([
                H1(Text('“Oh no, not again!”')),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ])
    )

if __name__ == '__main__':
    test()
