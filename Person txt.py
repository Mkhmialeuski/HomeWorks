class Person:
    def __init__(self, name, sername, age):
        self.__name = name
        self.__sername = sername
        self.__age = age

    def info(self):
        print(f'name = {self.__name}, sername = {self.__sername}, age = {self.__age}')

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if isinstance(age, str):
            try:
                age = int(age)
            except:
                age = 2
        self.__age = age

    def get_age(self):
        return self.__age


def sort(li):
    l = []
    for i in range(len(li)):
        s = li[i].split(' ')
        temp = []
        for k in s:
            temp.append(k)
        g = Person(temp[0], temp[1], int(temp[2]))
        l.append(g)
        temp.clear()
    return l


def older(li, age):
    li1 = []
    for p in li:
        if p.get_age() > age:
            li1.append(p)
    return li1


f = open('input.txt', 'r+', encoding='utf-8')
li = []
for i in f:
    i = i.replace('\n', '')
    s = i.split(' ')
    li.append(i)
li = sort(li)
li = older(li, 18)
for i in li:
    i.info()
