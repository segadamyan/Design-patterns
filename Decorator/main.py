from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        """Do some necessary steps"""
        print('Do something')
        return self._component.operation()


if __name__ == "__main__":
    simple = ConcreteComponent()

    decorator = Decorator(simple)
    decorator.operation()
    print("Client: Now I've got a decorated component:")
