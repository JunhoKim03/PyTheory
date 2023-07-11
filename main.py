import os
import random
import shutil
import functools

from classes import *

seperator = '___________'

# keyboard argument

print(seperator)


def helloAlex(fname, who, lname):
    print("Hi " + fname + " " + who + " " + lname)


helloAlex(lname="Pizzaz", fname="Zack", who="Zuzzezo")

# nested function calls = function calls inside other function calls

print(seperator)

print('A positive whole number of this would be', round(abs(float(input("Enter a negative decimal:")))))

# scopes = The region that a variable can be global and local

poo = "POO"


def PrintPoo():
    pooo = "POO"  # pooo variable can only be used inside of the function
    print(pooo)


# If I were to delete the local pooo, then the print(poo) would print the global poo

# args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of
#        arguments and can be named however you want

print(seperator)


def add(*args):
    sum = 0
    args = list(args)
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))

# kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying
# amount of arguments and can be named however you want

print(seperator)


def HelloWorld(**kwargs):  # <-- This is an item
    """print("Hello "+kwargs["First"]+" "+kwargs["Middle"]+kwargs["Last"])"""
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
    # more efficient and smart


HelloWorld(First=" Alex", Middle="", Last="Kim")

print('')

# str.format() = optional method that gives users more control when displaying an output

print(seperator)

animal = "cow"
item = "moon"
# print("The"+animal+"jumped over the"+item)

print("The {cow} jumped over the {0}".format(item, cow="cow"))

text = "The {} jumped over the {}"

text = text.format(animal, item)

print(text)

alex = "Alex"

print("Hello, my name is {:10}. Nice to meet you ".format(alex))

print("Hello, my name is {:^10}. Nice to meet you ".format(alex))

pi = 3.14159
number = 1000

# example:

print("The number pi is {:.2f}".format(pi))
# {:.2f} is the variable pi but only shows decimals till the tenth
print("The number is {:,}".format(number))
# this will print 1,000
print("The number is {:b}".format(number))
# this will print the binary value
print("The number is {:o}".format(number))
# this will print the octal value
print("The number is {:X}".format(number))
# this will print the hexadecimal
print("The number is {:E}".format(number))
# This will print the scientific notation

# random

dice = random.randint(1, 6)
print(dice)

RandomList = ['rock', 'paper', 'scissors']
RandomList = random.choice(RandomList)
print(seperator)
print(RandomList)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
print(seperator)
random.shuffle(cards)
# This will randomize the order of the cards
print(cards)

# exception = event detected during execution that interrupt the flow of a program

print(seperator)

try:
    numerator = int(input('Enter a number:'))
    denominator = int(input('Enter a denominator:'))
    result = numerator / denominator
except ZeroDivisionError as ZeroRule:
    print('You can\'t divide by zero you idiot!')
except ValueError as NotaNumber:
    print('Enter a number plz')
except Exception:
    print('Something went wrong :(')
else:
    print(result)
finally:
    print('This will always execute.')

# files

print(seperator)

a_path = 'C:\\Users\\user\\Desktop\\code.txt.txt'

if os.path.exists(a_path):
    print('That location exists!')
    if os.path.isfile(a_path):
        print('This path is a file')
        # this will see if this path is a file
    elif os.path.isdir(a_path):
        print('That is a directory.')
        # this will find out if the path is a directory/folder
else:
    print('That location does not exist!')

# file(how to read it)

print(seperator)

try:
    with open('text.txt',
              'r') as file:  # if this were tto be in your computer file you should add the location in the parenthesis
        print(file.read())
        # the 'withopen' function will automatically close the function, meaning that you will have to call the
        # 'withopen' function again in order to edit it after you are done with the function
except FileNotFoundError:
    print('The file is not found :(')

# file(how to write it)

print(seperator)

text = 'Python is very cool '

with open('text.txt', 'a') as file:  # 'a' keeps what's in the file; then writes it
    file.write(text)

with open('text.txt', 'w') as file:  # 'w' deletes what's in the file; then writes it
    file.write(text)

# file(how to copy it)

# copyfile() = copies content of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata ( file's creation and modification times)


shutil.copyfile('text.txt', 'copy.txt'
                # because the name is not modified,the file is not
                # reduplicated, it will be located in the python file
                )  # there are two arguments, src[original] and dst[new]

# file(how to move it)

source = 'test.txt'
destination = 'C:\Jk the fav child\Desktop\EAPP'

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source + ' was moved')
except FileNotFoundError:
    print(source + ' was not found.')

# file(how to delete it)

path = 'Text Folder'  # Instead, use Text Folder/test.txt

# this program cannot delete empty folders
try:
    # os.remove(path)
    # shutil.rmtree(path) consider this file as dangerous since it deletes the folder and all of its files
    os.rmdir(path)  # this will result in an os error since the folder contains files, if it did not, it would work
except FileNotFoundError:
    print('{}was not found'.format(path))
except PermissionError:
    print('You do not hav the permission to delete {}'.format(path))
except OSError:
    print('you cannot delete that folder since it contains a file')
else:
    print(path + 'was deleted')

# module = a file containing python code. May contain functions, classes, etc


# used with modular programming, which is to separate program into parts

# help('module will show you all the modules in python)

# classes

print(seperator)

car_1 = Car('Ferrari', 'GTC4 Lusso', 2022, 'Red')  # DISCLAIMER: Car_1 and Car will both use .(for instance)drive

motorbike = Car('Dodge', 'Tomahawk', 2003, 'Grey')

motorbike.wheels = 2

print(car_1.make)
print(motorbike.make)

car_1.drive()

motorbike.stop()

print(Car.wheels)  # This will display the motorbike's, and the car's number of wheels

# method chaining

print(seperator)

car_1.drive().stop()

# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

square = Square(3, 3)
cube = Cube(3, 5, 3)

square.area()
cube.volume()

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

print(seperator)


# vehicle = Vehicle()
# vehicle.drive | it is an abstract class, so it can't be used


# tip_1


def change_color(car_1, color):
    car_1.color = color


change_color(car_1, "purple")

# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

person = Person()
rabbit = Rabbit()

person.eat(rabbit)

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# example:

print(seperator)

print(happy := True)

# why it is useful:

'''  foods = list() 
     while True:
     food = input('What food do you like?:')
     if food == 'quit':
         break
     foods.append(food)  '''

foods = list()
print('')
while food := input('What food do you like?: ') != 'quit':
    foods.append(foods)

# function as variable

print(seperator)


def hello():
    print('Hello')


# print(hello) would make print the memory address in hexadecimal code

hi = hello  # there are no parentheses as hello is the memory address of hello()

print(hi)  # This will print the function address
hi()  # This function will give me Hello as I am calling the memory address.
# memory address() = hello(), thus making it a variable that could be used as a function

write = print
write('Write function was created with the same memory as the print function')

# Higher Order Function = a function that either:
#                         1. accepts a function as an argument
#                         or
#                         2. returns a function
#                         (in python, functions are also treated as objects)


# example 1:

print(seperator)


def ALLCAPS(Text):
    return Text.upper()


def lower(Text):
    return Text.lower()


def Helllo(func):
    Text = func("Hello")
    print(Text)


Helllo(ALLCAPS)
Helllo(lower)

# example 2:

print(seperator)


def divisor(X):
    def dividend(Y):
        return Y / X

    return dividend


divide = divisor(2)
print(divide(10))  # value of the dividend while X still = 2

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw away)
#                   used insort, filter, map functions

print(seperator)

# def double(x):
#       x + 2

double = lambda z: z + 2

print(double(2))

# iterable = a str, list, set, tuple or a dictionary

# sort()method  = used with lists
# sorted() function =  used with iterables


students = ["Alex", "ALexis", "Alexa", "Alice"]

# students.sort will order it alphabetically
# students.sort(reverse=False) sort method only has a few iterables(key and reverse)
# It also only works for lists
# sorted = students.sorted() will create a sorted version of the students list

sorted_students = sorted(students, reverse=False)  # It will sort it alphabetically

print(sorted_students)

students = [("Alex", "A", 100),
            ("Martin", "F", 1)]

grade = lambda grades: grades[1]
students.sort(key=grade)  # will sort the tuples by their grades
# students.sort() will sort the tuples by their first variable

# map() = applies a function to each item in an iterable (list, tuples, etc) / transforms an item
#
# map(function, iterable)

store = [('shirt', 20.00),
         ('jeans', 25.00),
         ('jacket', 50.00),
         ('shoes', 10.00)]

euro_conv = lambda data: (data[0], data[1] * 0.82)  # the data has no value

store_euros = list(map(euro_conv, store))

# filter() = creates a collection of elements from an iterable for which a function returns
#
# filter(functions,iterable)
#
# kinda like a search engine

gay_or_not = [('martin', True),
            ('danish', False)]

gay = lambda data: data[1] == True

gay_bud = list(filter(gay, gay_or_not))

print(gay_bud)

# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value is remains
#
# reduce(function, iterable)

letters = ['H', 'E', 'L', 'L', 'O']
bro = functools.reduce(lambda x, y: x + y, letters)
print(bro)

factorials = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorials)
print(result)

# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

'''squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)'''

squares = [i*i for i in range(1,11)]
print(squares)

student_grades = [100,90,80,70,60,50,40,30,0]

# passed_ students = list(filter(lambda x; x >= 60]

# passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "FAILED" for i in student_grades]

print(passed_students)