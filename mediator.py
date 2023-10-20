#!/usr/bin/python3

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from enum import Enum

class Region(Enum):
    NORTHEAST = 1
    MIDWEST = 2
    SOUTH = 3
    WEST = 4

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
    _name: str = ""
    _observers: List[Observer] = []
    def __init__(self, name) -> None:
        self._name=name
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    def notify(self, region) -> None:
        for observer in self._observers:
            if observer._region == region:
                observer.update(self)
    def message(self, msg, region) -> None:
        print(f"{self._name} says {msg} in the {region.name}, USA")
        self.notify(region)

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class City(Observer):
    _name: str = ""
    _region: Region = 0;
    def __init__(self, name, region) -> None:
        self._name=name
        self._region=region
    def update(self, subject: Subject) -> None:
        print(f"{self._name} was updated")

if __name__ == "__main__":
    nws = Agency("Nation Weather Service")
    cities=[]
    cities.append(City("New York City",Region.NORTHEAST))
    cities.append(City("Los Angeles",Region.WEST))
    cities.append(City("Chicago",Region.MIDWEST))
    cities.append(City("Houston",Region.SOUTH))
    cities.append(City("Phoenix",Region.WEST))
    cities.append(City("Philidelphia",Region.NORTHEAST))
    for city in cities:
        nws.attach(city)
    nws.message("it's windy",Region.MIDWEST)
    nws.message("it's sunny",Region.NORTHEAST)
    nws.message("it's snowy",Region.WEST)
