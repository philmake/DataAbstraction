"""
Hypothesis driven debugging: making careful educated guesses, with plans for how to validate or invalidate
them
"""

"""
Write tests - run tests - FAIL - implement - PASS

Test suite is the collection of test cases that, together, thoroughly (though not 100 % exhaustively -- that's 
impossible for all but the most trivial cases) test the data abstraction. 

create a test case for everything happening in the effects clause, and create a test case for each combination of 
inputs and outputs.

create test case such that each branch of your method is followed (this is loosely related to branch coverage,
though at this stage we are just checking branches generally, since we do not yet have an implementation 
against which to design a test case with proper branch coverage)

write test cases to test the edges of ranges (boundary checking) to check for typos in range checks or 
conditional statements.

test case should be named after the method they are testing, and also after the scenario they are testing 
to help you keep track of what yoi have tested. (Test<method name><scenario description>)

test cases always specify the inputs, and the expected outcome 
"""

"""
test_insert_not_alredy_there: insert # not already there
outcome: # appears in the test


test_insert_already_there: insert # already there
outcome: # appears in set ONCE
"""


class MySet:

    def __init__(self):
        self.__m_list = []
        pass

    def insert(self, num=0):
        """
        Modifies: this
        Effects: insert the integer into the set, unless it's already there, in which case it does nothing
        """
        if self.contains(num=num):
            pass
        else:
            self.__m_list.append(num)
        pass

    def get_size(self):
        return len(self.__m_list)

    def contains(self, num):
        return num in self.__m_list

    def remove(self, num):
        self.__m_list.remove(num)
        pass

    pass


class Usage:

    def run(self):
        mySet = MySet()
        mySet.insert(num=3)
        print("Does the set contain number 3? {}".format(mySet.contains(num=3)))
        print("The size of the set is: {}".format(mySet.get_size()))
        mySet.remove(3)
        print("Does the set contain number 3? {}".format(mySet.contains(num=3)))
        print("The size of the set is: {}".format(mySet.get_size()))
        pass

    pass


class Human:

    def __init__(self, name):
        self.__name = name
        pass

    def get_name(self):
        return self.__name

    pass


class WhiteMan(Human):

    # def __init__(self, name):
    #     super(WhiteMan, self).__init__(name=name)
    #     pass

    def says(self):
        return "Hello, I'm a white man. My name is {0}".format(self.get_name())

    pass


if __name__ == "__main__":
    use = Usage()
    use.run()

    # humam = Human("Filip")
    # print(humam.get_name())
    myman = WhiteMan(name='Filip')
    print(myman.says())


