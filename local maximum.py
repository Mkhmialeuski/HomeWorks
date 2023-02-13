n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in range(len(l) - 1):
    if i == 0:
        continue
    elif l[i - 1] < l[i] > l[i + 1] < 0:
        print(l[i])
