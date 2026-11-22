import math

goods = [
    [1, "кеды", 2500],
    [2, "ботинки", 4800],
    [3, "сандалии", 1900]
]
id_text = input("ID товара: ")
price_text = input("Новая цена: ")

try:
    product_id = int(id_text)
    price = float(price_text)
    found = False
    for item in goods:
        if item[0] == product_id:
            found = True
            if price >= 0 and math.isfinite(price):
                item[2] = price

    if found == False:
        print("Ошибка: товар не найден")
    elif price < 0 or math.isfinite(price) == False:
        print("Ошибка: неверная цена")
    else:
        for item in goods:
            print(item[0], "—", item[1], "—", item[2], "руб.")
except ValueError:
    print("Ошибка: неверный ID или цена")
