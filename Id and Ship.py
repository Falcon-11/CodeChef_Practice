t = int(input())

for i in range(t):
    s = input()

    dict1 = {
        "B": "BattleShip",
        "b": "BattleShip",
        "C": "Cruiser",
        "c": "Cruiser",
        "D": "Destroyer",
        "d": "Destroyer",
        "F": "Frigate",
        "f": "Frigate"
    }

    print(dict1[s])