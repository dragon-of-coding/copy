goods = {
    "A1": ["кеды", 2500, 10],
    "A2": ["ботинки", 4800, 20],
    "A3": ["сандалии", 1900, 0]
}
sku = input("Артикул: ")

if sku in goods:
    item = goods[sku]
    price = item[1]
    discount = item[2]
    final_price = price * (100 - discount) / 100
    print("Название:", item[0])
    print("Исходная цена:", format(price, ".2f"), "руб.")
    print("Итоговая цена:", format(final_price, ".2f"), "руб.")
else:
    print("Товар не найден")
