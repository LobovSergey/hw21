from errors import BadPoints
from request import Request
from shop import Shop
from store import Store
from utils import list_message
from time import sleep


def users_message():
    print('Добрый день. Для корректной доставки введите данные.')

    while True:
        user_msg = input('Введи строку формата "Доставить (колчиство) (товар) (отправление) (назначение)"')
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
    shop_dict = {'шоколад': 2,
                 'яблоко': 5}
    storage_dict = {'шоколад': 2}
    shop = Shop(shop_dict)
    store = Store(storage_dict)
    while True:
        user_request = Request(users_message(), storages)
        move_request = {user_request.product: user_request.amount}

        if user_request.departure == storages[1] and user_request.departure != user_request.arrival:
            store.remove(user_request.product, user_request.amount)
            sleep(1)
            shop.add(user_request.product, user_request.amount)
            sleep(1)
            print('На складе')
            list_message(store.get_items())
            print('В магазине')
            list_message(shop.get_items())
        elif user_request.departure == storages[2] and user_request.departure != user_request.arrival:
            shop.remove(user_request.product, user_request.amount)
            sleep(1)
            store.add(user_request.product, user_request.amount)
            sleep(1)
            print('В магазине')
            list_message(shop.get_items())
            print('На складе')
            list_message(store.get_items())
        else:
            raise BadPoints('Некорректные пути отправления/получения')
        while True:
            sleep(1)
            flag = input('Продолжить перемещения? Да/Нет').lower()
            if flag == 'нет':
                quit()
            elif flag == 'да':
                break
            else:
                print("Ничего не понятно. Повторю запрос")

