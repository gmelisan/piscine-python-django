import sys
import re
import os

def produce_html(template, settings):
    for key, value in settings.items():
        tmp = '{' + key + '}'
        replace = str(value)
        if isinstance(value, str):
            replace = value
        elif isinstance(value, list):
            replace = '<ul>\n'
            for item in value:
                replace += '<li>' + item + '</li>\n'
            replace += '</ul>\n'
        template = re.sub(tmp, replace, template)
    return template
        
def start():
    assert(len(sys.argv) == 2), 'Should be 1 parameter'
    assert(os.path.exists(sys.argv[1])), 'File not exists'
    assert(sys.argv[1].endswith('.template')), 'Wrong extension'
    assert(os.path.exists('settings.py')), 'File "settings.py" not found'
    settings = {}
    template = ''
    with open('settings.py') as sf:
        content = sf.read()
        g = {}
        exec(content, g, settings)
    with open(sys.argv[1]) as f:
        template = f.read()
    html = produce_html(template, settings)
    filename = sys.argv[1].split('.')
    with open(filename[0] + '.html', 'w') as of:
        of.write(html)

def print_error_with_usage(s):
    usage = 'Usage: python3 {} *.template'.format(sys.argv[0])
    print('Error: ' + str(s))
    print(usage)

if __name__ =='__main__':
    try:
        start()
    except AssertionError as error: # no args, wrong extension
        print_error_with_usage(error)
    except OSError as error:    # File not found, wrong permission
        print_error_with_usage(error)
    except Exception as error:
        print(error)
