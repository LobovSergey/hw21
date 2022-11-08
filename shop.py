from store import Store


class Shop(Store):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)
        self.__items = items
        self.__capacity = capacity

    def __repr__(self):
        return f"Операция Магазин"

    def add(self, title, qnt):
        if self.get_unique_items_count() < 5:
            if self.get_free_space() > qnt:
                if title not in self.__items:
                    self.__items[title] = qnt
                else:
                    self.__items[title] += qnt
                    self.__capacity += qnt
                print(f'Курьер доставил {qnt} {title} в магазин')
            else:
                print('Недостаточно места на складе')

    def remove(self, title, qnt):
        if self.get_free_space() < qnt:
            print(f'Недостаточно {title} на складе, попробуйте заказать меньше')
        else:
            self.__items[title] -= qnt
            self.__capacity -= qnt
            print(f'Курьер забрал {qnt} {title} из магазина')

    def get_items(self):
        return self.__items
