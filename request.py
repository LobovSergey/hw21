from errors import BadStorageRequest


class Request:
    def __init__(self, message: str, storages: dict):
        split_msg = message.split(' ')
        if split_msg[-1] and split_msg[-3] in storages.values():
            self.amount = int(split_msg[1])
            self.product = split_msg[2]
            self.departure = split_msg[-3]
            self.arrival = split_msg[-1]
        else:
            raise BadStorageRequest('Введены не существующие точки отправления/назначения')


