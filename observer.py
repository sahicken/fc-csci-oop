from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def notify(self) -> None:
        pass

class Agency(Subject):
    _state: str = ""
    _name: str = ""
    _observers: List[Observer] = []
    def __init__(self, name) -> None:
        self._name=name
    def attach(self, observer: Observer) -> None:
        print(f"{self._name}: Attached an observer.")
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        print(f"{self._name}: Removed an observer.")
        self._observers.remove(observer)
    def notify(self) -> None:
        print(f"{self._name}: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    def announcement(self, state) -> None:
        self._state = state
        print(f"{self._name}: Announces {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class City(Observer):
    _name: str = ""
    def __init__(self, name) -> None:
        self._name=name
    def update(self, subject: Subject) -> None:
        print(f"{self._name} was updated")

if __name__ == "__main__":
    nws = Agency("Nation Weather Service")
    nyc = City("New York City")
    nws.attach(nyc)
    lax = City("Los Angeles")
    nws.attach(lax)
    chi = City("Chicago")
    nws.attach(chi)
    nws.announcement("it's windy in the Midwest")
    nws.detach(nyc)
    nws.announcement("it's sunny in New England")
    nws.announcement("it's snowy in the Southwest")
