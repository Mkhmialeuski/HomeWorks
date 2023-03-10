n = int(input())
s = [[0 for i in range(n)] for k in range(n)]
number = 0
x = 0
for i in range(n):
    x = i
    for k in range(n):
        if x > 0:
            s[i][k] = x
            x -= 1
        else:
            s[i][k] = number
            number += 1
    number = 0
for i in range(n):
    for k in range(i,i+1):
        s[i][k] = 0
for i in s:
    print(i)
