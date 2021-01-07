t = int(input())

for i in range(t):
    N = int(input())

    S = 0

    while N != 0:
        r = N % 10
        N = N // 10
        S = (S * 10 + r)
    print(S)