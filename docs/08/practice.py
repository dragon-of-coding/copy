goods = [
    ["A1", "кеды", 8],
    ["A2", "ботинки", 2],
    ["A3", "сандалии", 5]
]

for i in range(len(goods)):
    for j in range(len(goods) - 1):
        if goods[j][2] > goods[j + 1][2]:
            temp = goods[j]
            goods[j] = goods[j + 1]
            goods[j + 1] = temp

for item in goods:
    print(item[0], "—", item[1], "—", item[2], "пар")
print("Минимальный остаток:", goods[0][1])
