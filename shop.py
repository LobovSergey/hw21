from abstract_storage import Storage
from errors import NotEnoughAmount


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
            raise NotEnoughAmount(f'Не хватает места в свободном доступе')
        else:
            if title not in self._items or self._items[title] < qnt:
                raise NotEnoughAmount(f'Не хватает {title} в свободном доступе или отсутствует на складе')
            else:
                self._items[title] -= qnt
                self._capacity -= qnt
                print(f'Курьер забрал {qnt} {title} со склада')

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
