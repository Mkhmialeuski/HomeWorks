x1 = int(input('X1'))
y1 = int(input('Y1'))
x2 = int(input('X2'))
y2 = int(input('Y2'))

if x1 == x2 or y1 == y2:
    print('Bit')
elif abs(x1 - x2) == abs(y1 - y2):
    print('Bit')
else:
    print('No Bit')