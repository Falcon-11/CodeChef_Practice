t = int(input())

for i in range(t):
    A, B = map(int, input().split())

    C = A % B
    print(C)