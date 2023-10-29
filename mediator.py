#!/usr/bin/python3

# ^^ the shebang allows direct execution

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
# now we need to add enums
from enum import Enum

# seems like a suitable data structure for encapsulation
# this is a simple example of the MEDIATOR pattern
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
    # since behavior from city is used, this should be list of cities
    _observers: List[City] = [] # python doesn't enforce typing
    def __init__(self, name) -> None:
        self._name=name
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    def notify(self, region) -> None:
        for observer in self._observers:
            # let's ONLY notify the regions of concern
            if observer._region == region:
                observer.update(self)
    def message(self, msg, region) -> None:
        print(f"{self._name} says {msg} in the {region.name}, USA")
        # notice that the message isn't passed
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
        # just confirm the update happened
        print(f"{self._name} was updated")

# only if the program is a the main program will the below execute
if __name__ == "__main__":
    nws = Agency("Nation Weather Service")
    cities=[]
    cities.append(City("New York City",Region.NORTHEAST))
    cities.append(City("Los Angeles",Region.WEST))
    cities.append(City("Chicago",Region.MIDWEST))
    cities.append(City("Houston",Region.SOUTH))
    cities.append(City("Phoenix",Region.WEST))
    cities.append(City("Philidelphia",Region.NORTHEAST))
    # we could add any number of cities
    for city in cities: # we MUST attach them
        nws.attach(city)
    # all the messages/notices are sent to the right places
    nws.message("it's windy",Region.MIDWEST)
    nws.message("it's sunny",Region.NORTHEAST)
    nws.message("it's snowy",Region.WEST)
