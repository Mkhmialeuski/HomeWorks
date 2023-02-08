a = int(input())
degree = 0

while 2 ** degree <= a:
    if 2 ** degree == a:
        print('Yes')
        break
    degree += 1
else:
    print('No')