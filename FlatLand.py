t = int(input())

for i in range(t):
    n = int(input())

    count = 0

    while n > 0:
        k = int(n ** (1 / 2))
        count += 1

        n = n - int(k ** 2)

    print(count)