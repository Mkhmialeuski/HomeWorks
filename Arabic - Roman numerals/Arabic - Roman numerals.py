class Number:
    def __init__(self, number):
        self.__number = number

    def info(self):
        print(f'{self.__number} нужно перевсти в римскую цифру')

    def get_numbers(self):
        return self.__number

    def set_numbers(self, number, li=list):
        l = str(number)
        k = ''
        while len(l) > 0:
            for i in range(len(li) - 1):
                if int(l) < int(li[i + 1][0]):
                    k = k + str(li[i][1])
                    l = l[1:]
                    break
        return k


f = open('input.txt', 'r+')
l = []
for i in f:
    i = i.replace('\n', '')
    s = i.split(' ')
    l.append(s)
a = Number(5)
print(a.set_numbers(158, l))
