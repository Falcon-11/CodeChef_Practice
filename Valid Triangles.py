t = int(input())

for i in range(t):
    A, B, C = map(int, input().split())

    angle = A + B + C

    if angle == 180:
        print('YES')
    else:
        print('NO')