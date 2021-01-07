t = int(input())
for i in range(t):
    D, N = map(int, input().split())
    k = 0

    sum1 = sum(range(0, N + 1))

    while k != D:
        sum2 = sum(range(0,sum1+1))
        k += 1

print(sum2)