from errors import BadPoints
from request import Request
from shop import Shop
from store import Store


def users_message():
    print('Добрый день. Для корректной доставки введите данные.')

    while True:
        user_msg = f"Доставить {int(input('Количество: '))} {input('Товар: ').lower()}" \
                   f" из {input('Точка отправления(склад/магазин): ').lower()}" \
                   f" в {input('Точка назначения(склад/магазин): ').lower()}"
        print(user_msg)
        correct = input('Все верно? Да/Нет').lower()
        if correct == 'да':
            print()
            return user_msg
        elif correct == 'стоп':
            print('end programm')
            quit()
        elif correct == 'нет':
            print('Введитие данные заново')
        else:
            print('Некорректный ответ. Введитие данные заново')


if __name__ == "__main__":
    storages = {1: 'склад',
                2: 'магазин'}
    shop_dict = {'шоколад': 2}
    user_request = Request(users_message(), storages)
    move_request = {user_request.product: user_request.amount}
    shop = Shop(shop_dict)
    store = Store(shop_dict)
    print(shop)
    print(store)
    if user_request.departure == storages[1] and user_request.departure != user_request.arrival:
        store.remove(user_request.product, user_request.amount)
        shop.add(user_request.product, user_request.amount)
        store.get_items()
        store.get_free_space()
        store.get_unique_items_count()
        shop.get_items()
        shop.get_free_space()
        shop.get_unique_items_count()
    elif user_request.departure == storages[2] and user_request.departure != user_request.arrival:
        shop.remove(user_request.product, user_request.amount)
        store.add(user_request.product, user_request.amount)
        shop.get_items()
        shop.get_free_space()
        shop.get_unique_items_count()
        store.get_items()
        store.get_free_space()
        store.get_unique_items_count()
    else:
        raise BadPoints('Некорректные пути отправления/получения')
