t = int(input())

for i in range(t):
    N = int(input())

    arr = list(map(int, str(N)))

    result = arr[0] + arr[-1]
    print(result)