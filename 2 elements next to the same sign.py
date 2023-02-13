n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in range(len(l)-1):
    if l[i] < 0 and  l[i + 1] < 0:
        print(l[i],l[i +1])
        break
    if l[i] > 0 and l[i + 1] > 0:
        print(l[i], l[i + 1])
        break
