from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict, capacity):
        pass

    @abstractmethod
    def add(self, title, qnt):  # None
        pass

    @abstractmethod
    def remove(self, title, qnt):  # None
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
