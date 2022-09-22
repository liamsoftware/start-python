# Abstract class - template class that cannot be instantiated.
#   Contains one or more abstract methods.
#   Abstract methods must be overridden and implemented in subclass.
# Abstract method - method defined but is not implemented.

from abc import ABC, abstractmethod


class Truck(ABC):
    @abstractmethod
    def price(self):
        pass


class CementTruck(Truck):
    def price(self):
        print('120E per hour')


class ArticulatedTruck(Truck):
    def price(self):
        print('100E per hour')


truck1 = CementTruck()
truck1.price()
truck2 = ArticulatedTruck()
truck2.price()

# Trying to create a Truck object will result in an error
truck3 = Truck()
