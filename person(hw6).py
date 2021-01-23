#!/usr/bin/env python3
"""
    Написать код на Python который имплементирует классы Person,
    Programmer, Dancer. Написать функцию main в которой создаются объекты из
    класса Programmer, Dancer и запускает по одному любому методу из каждого
    объекта.
"""


class Person:
    name = ""
    designation = ""

    def learn(self):
        print("Learning...")

    def walk(self):
        print("I am in walking...")

    def eat(self):
        print("Eating, don`t disturb!")


class Singer(Person):
    band_name = ""

    def sing(self):
        print("la la la")

    def play_guitar(self):
        print("Playing guitar...")


class Dancer(Person):
    group_name = ""

    def dancing(self):
        print("I am dancing Hip-Hop...")

    def sing(self):
        print("I am not sing, I am dance...")


class Programmer(Person):
    company_name = ""

    def codding(self):
        print("I am codding in Python...")

    def use_spaces(self):
        print("I am use spaces, not tabs....")


if __name__ == '__main__':
    singer = Singer()
    singer.sing()
    singer.learn()
    dancer = Dancer()
    dancer.dancing()
    dancer.learn()
    programmer = Programmer()
    programmer.codding()
    programmer.learn()
