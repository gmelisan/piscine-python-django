# returns list like:
# example = [
#     {
#         'name': 'Hydrogen'
#         'number': 1
#         'position': 0,
#         'small': 'H',
#         'molar': 1.00794,
#         'electron': [1]
#     },
#     {
#         ...
#     },
#     ...
# ]

def parse_file(filename):
    res = []
    f = open(filename)
    while True:
        line = f.readline()
        if not line:
            break
        list1 = line.split('=')
        name = list1[0].strip()
        list2 = list1[1].split(',')
        list3 = list2[0].split(':')
        position = int(list3[1])
        list3 = list2[1].split(':')
        number = int(list3[1])
        list3 = list2[2].split(':')
        small = list3[1].strip()
        list3 = list2[3].split(':')
        molar = float(list3[1])
        list3 = list2[4].split(':')
        list4 = list3[1].split(' ')
        electron = []
        for e in list4:
            electron.append(int(e))
        res.append({
            'name': name,
            'number': number,
            'position': position,
            'small': small,
            'molar': molar,
            'electron': electron
        });
    f.close()
    return res

# generates list of lists of element
# with empty element where it should not be placed
def generate_table(elements):
    table = []
    i = 0
    for period in range(0, 7):
        table.append([])
        for pos in range(0, 18):
            if elements[i]['position'] == pos:
                table[period].append(elements[i])
                i += 1
            else:
                table[period].append({})
    return table

def generate_header():
    str = '<!DOCTYPE html>\n'
    str += '<html lang="en">\n'
    str += '<head>\n'
    str += ' <meta charset="utf-8"/>'
    str += ' <title> Periodic table of elements </title>\n'
    str += ' <link rel="stylesheet" href="periodic_table.css">\n'
    str += '</head>'
    str += '<body>\n'
    str += '<div class="header">\n'
    str += ' <h1> Periodic table of elements </h1>\n'
    str += '</div>\n'
    return str

def generate_footer():
    return "</body>\n</html>\n"

def get_element_group_classname(e):
    g1 = [1, 6, 7, 8, 15, 16, 34]
    if e['number'] in g1:
        return "g1"
    g2 = [2, 10, 18, 36, 54, 86, 118]
    if e['number'] in g2:
        return "g2"
    g3 = [3, 11, 19, 37, 55, 87]
    if e['number'] in g3:
        return "g3"
    g4 = [4, 12, 20, 38, 56, 88]
    if e['number'] in g4:
        return "g4"
    g5 = [5, 14, 32, 33, 51, 52, 84]
    if e['number'] in g5:
        return "g5";
    g6 = [9, 17, 35, 53, 85, 117]
    if e['number'] in g6:
        return "g6"
    g7 = [13, 31, 49, 50, 81, 82, 83, 113, 114, 115, 116]
    if e['number'] in g7:
        return "g7"
    return "g8"

def generate_html_table(table):
    str = '<div class="pertab">' 
    str += "<table>\n"
    for row in table:
        str += " <tr>\n"
        for element in row:
            if element  != {}:
                tmp = ""
                tmp += '  <td class="{}">\n'
                tmp += '   <ul>\n'
                tmp += '    <li class="number">{}</li>\n'
                tmp += '    <li class="molar">{}</li>\n'
                tmp += '    <li class="small">{}</li>\n'
                tmp += '   </ul>\n'
                tmp += '   <h4 class="name">{}</h4>\n'
                str += tmp.format(get_element_group_classname(element),
                                  element['number'],
                                  element['molar'],
                                  element['small'],
                                  element['name'])
            else:
                str += '  <td>'
            str += "  </td>\n"
        str += " </tr>\n"
    str += "</table>\n"
    str += '</div>'
    return str

def save_html(table):
    f = open("periodic_table.html", "w")
    f.write(generate_header())
    f.write(generate_html_table(table))
    f.write(generate_footer())
    f.close()

def generate_css():
    str = ""
    str += 'div.header {\n'
    str += ' text-align: center;\n'
    str += ' font-size: 1.3vw;\n'
    str += '}\n'
    str += 'div.pertab {\n'
    str += ' position: relative;\n'
    str += ' top: 20;\n'
    str += ' width: 95vw;\n'
    str += ' margin: 0 auto;\n'
    str += '}\n'
    str += 'td {\n'
    str += ' text-align: center;\n'
    str += ' width: 5vw;\n'
    str += '}\n'
    str += 'ul {\n'
    str += ' margin: 0;\n'
    str += ' padding: 0;\n'
    str += '}\n'
    str += 'li.molar {\n'
    str += ' list-style-type: none;\n'
    str += ' font-size: 0.7vw;\n'
    str += ' text-align: right;\n'
    str += ' margin: 2px;\n'
    str += '}\n'
    str += 'li.number {\n'
    str += ' list-style-type: none;\n'
    str += ' font-size: 1vw;\n'
    str += ' text-align: left;\n'
    str += ' margin: 2px;\n'
    str += ' float: left;\n'
    str += '}\n'
    str += 'li.small {\n'
    str += ' list-style-type: none;\n'
    str += ' font-size: 1.3vw;\n'
    str += ' margin: 1.2vw;\n'
    str += ' padding: 0;\n'
    str += ' font-weight: bold;\n'
    str += ' text-align: center;\n'
    str += '}\n'
    str += 'h4.name {\n'
    str += ' font-size: 0.8vw;\n'
    str += ' text-align: left;\n'
    str += ' margin: 2px;\n'
    str += '}\n'
    str += 'td.g1 {\n'
    str += ' background-color: #ccff99;\n'
    str += '}\n'
    str += 'td.g2 {\n'
    str += ' background-color: #66ffff;\n'
    str += '}\n'
    str += 'td.g3 {\n'
    str += ' background-color: #ff6666;\n'
    str += '}\n'
    str += 'td.g4 {\n'
    str += ' background-color: #ffcc99;\n'
    str += '}\n'
    str += 'td.g5 {\n'
    str += ' background-color: #cccc99;\n'
    str += '}\n'
    str += 'td.g6 {\n'
    str += ' background-color: #ffff99;\n'
    str += '}\n'
    str += 'td.g7 {\n'
    str += ' background-color: #bfbfbf;\n'
    str += '}\n'
    str += 'td.g8 {\n'
    str += ' background-color: #ffcccc;\n'
    str += '}\n'
    return str
    
def save_css():
    f = open("periodic_table.css", "w")
    f.write(generate_css())
    f.close()

def start():
    elements = parse_file("periodic_table.txt")
    table = generate_table(elements)
    save_html(table)
    save_css()

if __name__ == '__main__':
    start()
