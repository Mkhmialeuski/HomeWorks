n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in range(len(l) - 1):
    if l[i] < l[i + 1]:
        print(l[i + 1])
