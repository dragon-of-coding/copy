from datetime import date

orders = {
    "Z1": "2026-12-01",
    "Z2": "2026-12-02",
    "Z3": "2026-12-03"
}
sku = input("Артикул заказа: ")
new_date = input("Дата (ГГГГ-ММ-ДД): ")

if sku not in orders:
    print("Заказ не найден")
elif len(new_date) != 10 or new_date[4] != "-" or new_date[7] != "-":
    print("Ошибка: неверный формат даты")
else:
    try:
        year = int(new_date[0:4])
        month = int(new_date[5:7])
        day = int(new_date[8:10])
        correct_date = date(year, month, day)
        if correct_date.isoformat() == new_date:
            orders[sku] = new_date
            print("Обновлённый заказ:", sku, orders[sku])
        else:
            print("Ошибка: неверная дата")
    except ValueError:
        print("Ошибка: неверная дата")
