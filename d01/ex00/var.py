def my_var():
    a = 42
    b = "42"
    c = "quarante-deux"
    d = 42.0
    e = True
    f = [42]
    g = {42: 42}
    h = (42,)
    i = set()

    print(str(a) + " has a type " + str(type(a)));
    print(str(b) + " has a type " + str(type(b)));
    print(str(c) + " has a type " + str(type(c)));
    print(str(d) + " has a type " + str(type(d)));
    print(str(e) + " has a type " + str(type(e)));
    print(str(f) + " has a type " + str(type(f)));
    print(str(g) + " has a type " + str(type(g)));
    print(str(h) + " has a type " + str(type(h)));
    print(str(i) + " has a type " + str(type(i)));

if __name__ == '__main__':
    my_var()
    
    
