from abc import ABC, abstractmethod


class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    def cook_dinner(self):
        raise NotImplementedError


class Mother(AbstractParent):

    def cook_dinner(self):
        print("Here is some chicken")

    def __init__(self):
        print("Mother constructor")

    def do_work(self):
        print("I'm working and nobody notice that")

    def do_house_work(self):
        print("Listen to music")


class Father(AbstractParent):

    def hello_friend(self):
        print("Hello dear")

    def __init__(self):
        print("Father constructor")

    def play_guitar(self):
        print("Guitar goes brrr")

    def do_house_work(self):
        print("Lay down")


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Mother.__init__(self)
        Father.__init__(self)

    def do_work(self):
        print("Why should i work?")


class Friend:
    def __init__(self):
        pass

    def go_away(self):
        print("Bye!")


def greet_mother(person: Mother):
    person.do_work()
    print("Mother came")


def greet_father(person: Father):
    person.play_guitar()
    print("Gimme beer!")


if __name__ == '__main__':
    daughter = Daughter()
    greet_father(daughter)
    greet_mother(daughter)
    daughter.hello_friend()
    daughter.cook_dinner()
    daughter.do_house_work()

    for x in [daughter]:
        x.do_house_work()

    #list
    povtor = ["matan", "history"]

    #tuple
    dont_touch = (12, 3.14, daughter)

    #set
    my_set = {45, 56, "count"}

    #Elsa set
    another_set = frozenset(["do", "re", "mi"])

    #dicitonary
    my_dict = {1: "first el", "2": "second el", (1, 2, 3): "tuple_key"}
