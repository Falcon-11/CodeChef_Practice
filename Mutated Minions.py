t = int(input())

for i in range(t):
    N, K = map(int, input().split())

    arr = map(int, input().strip().split())
    res = [i + K for i in arr]

    count = 0

    for i in res:
        if i % 7 == 0:
            count += 1

    print(count)