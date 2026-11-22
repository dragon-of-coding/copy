goods = [
    ["A1", "белые кеды", "Альфа"],
    ["A2", "зимние ботинки", "Альфа"],
    ["A3", "чёрные кеды", "Бета"]
]
query = input("Фрагмент названия: ").lower()
supplier = input("Поставщик: ").lower()
found = False

for item in goods:
    name_matches = query in item[1].lower()
    supplier_matches = supplier == "все поставщики"
    if item[2].lower() == supplier:
        supplier_matches = True

    if name_matches and supplier_matches:
        print(item[0], "—", item[1], "—", item[2])
        found = True

if found == False:
    print("Товары не найдены")
