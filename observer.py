from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# abstract base classes may include behavior before extending
# interfaces have zero behavior until a derived class impls them

class Subject(ABC):
    @abstractmethod # member fxns called methods in java/python
    def attach(self, observer: Observer) -> None:
        pass # this means do nothing
    @abstractmethod # annotation aren't required in python
    def detach(self, observer: Observer) -> None:
        pass # self is similar to this in C++
    @abstractmethod # returning None is like void
    def notify(self) -> None:
        pass

class Agency(Subject):
    _state: str = ""
    _name: str = ""
    # any observer could be in this list, not just cities, BE CAREFUL
    _observers: List[Observer] = [] # pointers/virtual fxns in C++
    # __init__ is python's constructor
    def __init__(self, name) -> None: 
        self._name=name # yes, you need self
    def attach(self, observer: Observer) -> None:
        # f-strings are awesome, please use them
        print(f"{self._name}: Attached an observer.")
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        print(f"{self._name}: Removed an observer.")
        self._observers.remove(observer)
    def notify(self) -> None:
        print(f"{self._name}: Notifying observers...")
        # this is how we will notify our list of observers
        for observer in self._observers:
            observer.update(self)
    # notice that this function is not from ABC of type Subject
    def announcement(self, state) -> None:
        self._state = state
        print(f"{self._name}: Announces {self._state}")
        # notify is a fxn all subjects impl.
        self.notify()

# begin our observer code
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

# we would say City extends Observer (an ABC)
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
    # why would new york be notified??
    nws.detach(nyc)
    nws.announcement("it's sunny in New England")
    nws.announcement("it's snowy in the Southwest")
