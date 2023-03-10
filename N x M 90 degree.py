n = 3
m = 4
l = [[11, 12, 13, 14],
     [21, 22, 23, 24],
     [31, 32, 33, 34]]
s = [[0 for i in range(n)] for k in range(m)]
for i in range(n):
    temp = []
    for j in range(i,i+1):
        for g in range(m):
            temp.append(l[j][g])

    for k in range(n,-1,-1):
        for h in range(m-2,i-1,-1):
            s[k][h] = temp[k]
    temp.clear()
#s.reverse()
for i in range(m):
    s[i].reverse()
for i in s:
    print(i)