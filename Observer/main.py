from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

import requests


class Subject(ABC):
    """
    Subject interface: declares a set of methods for managing subscribers.
    """

    def __init__(self):
        self._state = None

    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        """
        Subscribe to the subject.
        """
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        """
        Unsubscribe from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class UserSubject(Subject):
    _state: [User] = None

    __observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.__observers.append(observer)
        print("Subject: Subscribed an observer.")

    def unsubscribe(self, observer: Observer) -> None:
        self.__observers.remove(observer)
        print("Subject: Unsubscribed an observer.")

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self.__observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        response = requests.get("https://randomuser.me/api/")
        self._state = self.__map_to_user(response)

        self.notify()

    @staticmethod
    def __map_to_user(response):
        return [
            User(i['name']['first'] + i['name']['last'], i['gender'], i['location']['city'], i['location']['country'])
            for i in
            response.json()['results']]


class User:

    def __init__(self, name, gender, city, country):
        self.__name = name
        self.__gender = gender
        self.__city = city
        self.__country = country

    def __repr__(self):
        return f'{self.__name}, {self.__gender}, {self.__city}, {self.__country}'


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        print(repr(subject._state[0]))


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print(repr(subject._state[0]))


if __name__ == "__main__":
    subject = UserSubject()

    observer_a = ConcreteObserverA()
    subject.subscribe(observer_a)

    observer_b = ConcreteObserverB()
    subject.subscribe(observer_b)

    subject.some_business_logic()

    subject.unsubscribe(observer_a)

    subject.some_business_logic()
