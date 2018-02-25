"""
This module is meant to be an abstraction guidance for me and it's gonna help me to get to SpaceX - the coolest company
EVER
"""


class Try:

    def __init__(self):
        self.x = 0
        print("x val: {} and adr: {}".format(self.x, id(self.x)))
        pass

    def add_x(self, nx):
        print("nx val: {} and adr: {}".format(nx, id(nx)))
        print("x val: {} and adr: {}".format(self.x, id(self.x)))
        self.x = nx
        print("nx val: {} and adr: {}".format(nx, id(nx)))
        print("x val: {} and adr: {}".format(self.x, id(self.x)))
        pass

    def get_x_repr(self):
        return "x val: {} and adr: {}".format(self.x, id(self.x))

    pass


mTry = Try()
newx = 50
mTry.addx(newx)


class MyNewList:

    def __init__(self):
        self.__myList = list()
        pass

    def insert(self, num=0):
        """
        Requires: nothing (To be deleted from the documentation)
        Modifies: self
        Effects: inserts num if not already there, if num is there, does nothing
        :return:
        """
        pass

    def remove(self):
        """

        :return:
        """