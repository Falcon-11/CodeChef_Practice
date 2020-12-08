t = int(input())

for i in range(t):
    BS = int(input())

    if BS < 1500:
        HRA = (10 / 100) * BS
        DA = (90 / 100) * BS

    else:
        HRA = 500
        DA = (98 / 100) * BS

    GS = BS + HRA + DA

    print(GS)
