from abstract_storage import Storage


class Shop(Storage):

    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return f"Операция Магазин"

    def add(self, title, qnt):
        if self.get_unique_items_count() < 5:
            if self.get_free_space() > qnt:
                if title not in self._items:
                    self._items[title] = qnt
                else:
                    self._items[title] += qnt
                    self._capacity += qnt
                print(f'Курьер доставил {qnt} {title} в магазин')
            else:
                print('Недостаточно места на складе')

    def remove(self, title, qnt):
        if self.get_free_space() < qnt:
            print(f'Недостаточно {title} на складе, попробуйте заказать меньше')
        else:
            self._items[title] -= qnt
            self._capacity -= qnt
            print(f'Курьер забрал {qnt} {title} из магазина')

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
