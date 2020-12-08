t = int(input())

for i in range(t):
    N = int(input())

    d = 1
    count = 0

    while d != N + 1:
        N % d
        if N % d == 0:
            count += 1
        d += 1

    if count == 2:
        print("yes")
    else:
        print("no")