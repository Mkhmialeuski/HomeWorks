n = int(input())
l = []
count = 0
for i in range(n):
    l.append(int(input()))
for i in l:
    if i > 0:
        count += 1
print(count)
