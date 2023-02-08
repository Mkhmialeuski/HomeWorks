a = int(input())
degree = 0

while 2 ** degree <= a:
    print(2 ** degree)
    degree += 1
