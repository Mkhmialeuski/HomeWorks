x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 == x2 - 1 or x1 == x2 + 1) and (y1 == y2 - 2 or y1 == y2 + 2):
    print('bit')
elif (x1 == x2 - 2 or x1 == x2 + 2) and (y1 == y2 - 1 or y1 == y2 + 1):
    print('bit')
else:
    print('No bit')
