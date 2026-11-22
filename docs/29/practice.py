goods = {
    "A1": "кеды",
    "A2": "ботинки",
    "A3": "сандалии"
}
order_goods = ["A2"]
sku = input("Артикул товара: ")

if sku not in goods:
    print("Товар не найден")
elif sku in order_goods:
    print("Удаление запрещено: товар присутствует в заказе")
else:
    del goods[sku]
    print("Обновлённый каталог:")
    for key in goods:
        print(key, "—", goods[key])
