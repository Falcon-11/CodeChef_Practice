t = int(input())

for i in range(t):
    arr = []

    while t != 0:
        N = int(input())
        t -= 1
        arr.append(N)

    arr.sort()

    for i in arr:
        print(i)

