goods = [
    ["кеды", 4],
    ["ботинки", 9],
    ["сандалии", 1]
]
print("1 — По возрастанию")
print("2 — По убыванию")
choice = input("Команда: ")

if choice != "1" and choice != "2":
    print("Неверное направление сортировки")
else:
    for i in range(len(goods)):
        for j in range(len(goods) - 1):
            if choice == "1":
                if goods[j][1] > goods[j + 1][1]:
                    temp = goods[j]
                    goods[j] = goods[j + 1]
                    goods[j + 1] = temp
            else:
                if goods[j][1] < goods[j + 1][1]:
                    temp = goods[j]
                    goods[j] = goods[j + 1]
                    goods[j + 1] = temp

    for item in goods:
        print(item[0], "—", item[1])
