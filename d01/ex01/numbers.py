def start():
    f = open("numbers.txt")
    str = f.read()
    number_list = str.strip().split(",")
    for item in number_list:
        print(item)

if __name__ == '__main__':
    start()
