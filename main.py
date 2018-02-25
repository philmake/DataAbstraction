import testPy
# import copy

"""
Toto je ciste test, jestli mi funguje Pycharm a GitHub dohromady, tak snad bude.
"""

print("My new python script in PyCharm, hello {0}!".format("Filip"))
print("Hello again")

myHello = testPy.Hello()

text = myHello.print_all()
print(text)

# Data abstraction course
x = 10
y = 5
print("x je {0} x-adr: {1}, y je {2} y-adr: {3}".format(x, id(x), y, id(y)))
x = 50
z = x = 33
print("x je {0} x-adr: {1}, z je {2} z-adr: {3}".format(x, id(x), z, id(z)))

x = 60
print("x ma hodnotu {0} a je na adrese: {1}".format(x, id(x)))
ml = [0, 1, 2, 3, 4, 5, 6]


def my_fce(mx=0, lis=[]):
    nlis = lis[:]
    print("lis {0} a adresa je {1}, nlis {2} a adresa je {3}".format(lis, id(lis), nlis, id(nlis)))
    print("Uvnitr fce je hodnota {0} a adresa je {1}".format(mx, id(mx)))
    print(mx)
    mval = mx
    mx = 555
    print(mval)
    print("Uvnitr fce je hodnota {0} a adresa je {1}".format(mval, id(mval)))
    pass


my_fce(x)
x = 50


def new_try_fce(value1=0):
    """
    All immutable types are:
    > int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes
    All mutable types are:
    > list, dict, set, byte-array, user-defined classes (unless specifically made immutable)

    :param value1:
    :return:
    """
    value1 = 50
    return value1


val2 = 100
print("Returns {} and the original passed by immutable value is {}".format(new_try_fce(val2), val2))

"""
Boolean:
True/False

Numeric types:
int, float (usually implemented using C double), complex (real and imaginary part which are both floating point),
decimal, fractions

Sequence types:
list, tuple, range
"""
cmplx = 3+4j

print("Complex value: {}".format(cmplx))

val1 = 3.4 + 5.8

print("Hodnota po secteni 3.4 + 5.8 je {}".format(val1))


def chng_list(inList=[]):
    print("Original: {}".format(inList))
    del inList[:3]
    print("Modified passed list: {}".format(inList))
    pass


def chng_val(value=0):
    print("in fce x(value) id {}".format(id(value)))
    value = 60
    print("in fce x(value) id {}".format(id(value)))


myl = [0, 1, 2, 3, 4, 5, 6, 7]
chng_list(inList=myl)
print("List after function: {}".format(myl))

x = 50
print("x id {}".format(id(x)))
chng_val(x)
print("x id {}".format(id(x)))


def ml(*x):
    print(x)
    pass


ml(5, "Ahoj, jak se mas", "ale docela to jde")
ml()



def hello(name="Filip"):
    a = 50//30
    print(a)
    g = ['a', 'b', 'c', 0]
    del g[-1]
    g.pop(-1)
    g.remove('b')
    print(g)
    return "{} is a master in Pythoning!".format(name)


print(hello())
hello()


class Human:

    def __init__(self, name="Filip", age=1):
        self.__name = name
        self.__age = age
        pass

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        """
        spoji jmena a pricte vek druheho do puvodniho a vrati novy objekt
        :param other:
        :return:
        """
        name, age = other.__dict__.values()
        return Human(name= " + ".join([self.__name,name]), age=self.__age+age)

    pass


fhuman = Human()
ghuman = Human()
mhuman = Human('Tereza', 25)

print(fhuman)
print(mhuman)

pravda = fhuman is mhuman
print("Je inst Filip inst Tereza? {}".format(pravda))
pravda = fhuman == mhuman
print("Jsou si inst Filip z fhuman a inst Tereza z hhuman rovni? {}".format(pravda))
pravda = fhuman is ghuman
print("Je inst Filip inst Filip z ghuman? {}".format(pravda))
pravda = fhuman == ghuman
print("Jsou si inst Filip z fhuman a inst Filip z ghuman rovni? {}".format(pravda))
novyClovek = fhuman + ghuman
print(novyClovek)


a = 500
b = 501
a *= 2
a /= 2
z = 10
try:
    a = b * z
except NameError as error:
    print("What is the error? {}".format(str(error)))
    pass

print("Je a id:{} b id:{}? {}".format(id(a), id(b), a is b))
print("Josu si a a b rovni? {}".format(a == b))
