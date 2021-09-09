#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;') \
                                .replace('>', '&gt;') \
                                .replace('"', '&quot;') \
                                .replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    tag = ''                    # tag name
    tag_type = ''               # 'double' or 'simple'
    attr = {}                   # dict of attributes
    content = []                # list of elements inside tag

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        if not (self.check_type(content) or content is None):
            raise Elem.ValidationError
        if (tag_type != 'double' and tag_type != 'simple'):
            raise Elem.ValidationError
        if content == None:
            self.content = []
        elif (isinstance(content, Elem) or
              isinstance(content, Text)):
            self.content = [content]
        else:
            self.content = content
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = '<{}{}>{}</{}>' \
                .format(self.tag,
                        self.__make_attr(),
                        self.__make_content(),
                        self.tag)
        elif self.tag_type == 'simple':
            result = '<{}{} />' \
                .format(self.tag,
                        self.__make_attr())
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            s = str(elem)
            if len(s) != 0:
                result += s + '\n'
        result = '  '.join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ''
        
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
    class ValidationError(Exception):
        def __init__(self):
            self.message = 'Validation error'

        def __str__(self):
            return self.message


def test():
    html = Elem('html')
    
    head = Elem('head')
    title = Elem('title')
    title.add_content(Text('“Hello ground!”'))
    head.add_content(title)
    
    body = Elem('body')
    h1 = Elem('h1')
    h1.add_content(Text('“Oh no, not again!”'))
    img = Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'})
    body.add_content([h1, img])

    html.add_content([head, body])

    print(html)

if __name__ == '__main__':
    test()
