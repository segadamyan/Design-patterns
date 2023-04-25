from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def add_part_a():
        """Build part a"""

    @staticmethod
    @abstractmethod
    def add_part_b():
        """Build part b"""

    @staticmethod
    @abstractmethod
    def add_part_c():
        """Build part c"""

    @staticmethod
    @abstractmethod
    def build():
        """Return the final product"""


class Builder(IBuilder):
    """The Concrete Builder."""

    def __init__(self):
        self.__product = Product()

    def add_part_a(self):
        self.__product.parts.append('a')
        return self

    def add_part_b(self):
        self.__product.parts.append('b')
        return self

    def add_part_c(self):
        self.__product.parts.append('c')
        return self

    def build(self):
        return self.__product


class Product:
    def __init__(self):
        self.parts = []


class Director:

    @staticmethod
    def construct():
        """Constructs and returns the final product"""
        return Builder().add_part_a().add_part_b().add_part_c().build()


# Usage
PRODUCT = Director.construct()
print(PRODUCT.parts)
