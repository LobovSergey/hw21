from abstract_storage import Storage
from errors import NotEnoughAmount


class Store(Storage):

    def __init__(self, items: dict, capacity: int = 100):
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return f"Операция Склад"

    def add(self, title, qnt):
        if self.get_free_space() > qnt:
            if title not in self.get_items():
                self._items[title] = qnt
            else:
                self._items[title] += qnt
                self._capacity += qnt
            print(f'Курьер доставил {qnt} {title} на склад')
        else:
            print('Недостаточно места на складе')

    def remove(self, title, qnt):
        if self.get_free_space() < qnt:
            NotEnoughAmount(f'Не хватает места в свободном доступе')
        else:
            if self._items[title] >= qnt:
                self._items[title] -= qnt
                self._capacity -= qnt
                print(f'Курьер забрал {qnt} {title} со склада')
            else:
                raise NotEnoughAmount(f'Не хватает {title} в свободном доступе')

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
