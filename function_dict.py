def dic(n):
    A = {}
    for i in range(n):
        x = input("key")
        y = input('valeu')
        A[x] = y
    return A
n = int(input())
print(dic(n))

