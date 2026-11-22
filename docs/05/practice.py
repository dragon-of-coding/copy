goods = [
    ["A1", "кеды", "Север"],
    ["A2", "ботинки", "Вектор"],
    ["A3", "сандалии", "Север"]
]
query = input("Поиск: ").lower()
found = False

for item in goods:
    name = item[1].lower()
    maker = item[2].lower()
    if query in name or query in maker:
        print(item[0], "—", item[1], "—", item[2])
        found = True

if found == False:
    print("Товары не найдены")
