goods = [
    ["A1", "кеды", "Альфа"],
    ["A2", "ботинки", "Бета"],
    ["A3", "сандалии", "Альфа"]
]
supplier = input("Поставщик: ").lower()
found = False

for item in goods:
    if supplier == "все поставщики" or item[2].lower() == supplier:
        print(item[0], "—", item[1])
        found = True

if found == False:
    print("Товары не найдены")
