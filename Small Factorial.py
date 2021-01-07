t = int(input())

for i in range(t):
    N = int(input())

    k = 1

    while N >= 1:
        k = k * N
        N -= 1
    print(k)