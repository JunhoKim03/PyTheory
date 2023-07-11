from abc import ABC, abstractmethod


# IMPORTANT,

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    wheels = 4  # class variable

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable  #The self keyword allows you to manipulate
        self.model = model  # instance variable  #the method temporarily, for instance car_1 =
        self.year = year  # instance variable  #Car(make, model, year, color)
        self.color = color  # instance variable

    def drive(self):  # if you write Car.drive, it wouldn't work since self is not defined as Car is a class with a
        # make, model,year, and color defined by the coder. So instead create a variable that equals to the class +
        # make, mode, year, color
        print('This', self.make, self.model, 'is driving.')
        return self

    def stop(self):
        print('This', self.make, self.model, 'has stopped.')
        return self


# vehicle = Vehicle <-- won't work since Vehicle is an abstract class


class Animal:
    alive = True  # Since this is a class variable, when another class inherits it, it inherits the alive variable

    def eat(self, creature):
        print('This animal is eating a', creature)

    def sleep(self):
        print('This animal is sleeping')


class Person(Animal):

    def life(self, animal):
        animal.eat(self)
        animal.run(self)
        animal.nap()
        print('The {} is sleeping'.format(Person.__name__.lower()))




class Rabbit(Animal):
    def eat(self):
        print('This rabbit is eating grass')

    @staticmethod
    def nap():
        print('This rabbit is napping')

    @staticmethod
    def run():
        print('This rabbit is running')


class Fish(Animal):

    def swim(self):
        print('This fish can swim')


class Hawk(Animal):

    def fly(self):
        print('This Hawk can fly')


# This class is multiple inheritance and a multilevel inheritance class, since it inheritmore than one class,
# one which inherits from another

class Salmon(Fish):

    def tasty(self):
        print('This Salmon is tasty')


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)
        '''    def __init__(self, length, width):
               self.length = length
               self.width = width    '''

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        '''    def __init__(self, length, width, height):
               self.length = length
               self.width = width
               self.height = height    '''

    def volume(self):
        return self.length * self.width * self.height
