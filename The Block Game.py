t = int(input())

for i in range(t):
    N = int(input())

    k = [int(d) for d in str(N)]
    arr = []
    x = N

    while N != 0:
        r = N % 10
        N = N // 10
        arr.append(r)

    if arr == k:
        print("wins")
    else:
        print("loses")

