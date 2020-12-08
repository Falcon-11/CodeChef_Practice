t = int(input())

for i in range(t):
    n = int(input())

    c = 0

    c += n // 100
    n = n % 100

    c += n // 50
    n = n % 50

    c += n // 10
    n = n % 10

    c += n // 5
    n = n % 5

    c += n // 2
    n = n % 2

    c += n // 1
    n = n % 1

    print(c)
