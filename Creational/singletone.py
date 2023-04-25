class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python.
    Some possible methods include: base class, decorator, metaclass.
    This is a metaclass implementation
    """

    __instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        print(cls.__instances)
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class Singleton(metaclass=SingletonMeta):

    def some_business_logic(self):
        """
        Some business logic, which can be executed on its instance.
        """


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
