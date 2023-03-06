def input_list():
    a = []
    x = ''
    while True:
        x = input()
        try:
            if int(x) == 0:
                return a
            else:
                a.append(x)
        except:
            a.append(x)
a = input_list()
print(a)