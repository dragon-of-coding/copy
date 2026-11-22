goods = [
    ["A1", "белые кеды"],
    ["A2", "зимние ботинки"],
    ["A3", "чёрные кеды"]
]
query = input("Введите часть названия: ").lower()
found = False

for item in goods:
    name = item[1].lower()
    if query in name:
        print(item[0], "—", item[1])
        found = True

if found == False:
    print("Товары не найдены")
