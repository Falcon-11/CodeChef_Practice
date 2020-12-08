t = int(input())

for i in range(t):
    A, B, C = map(int, input().split())

    arr = [A, B, C]

    arr.sort()

    print(arr[1])