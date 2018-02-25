print("Test PY")


class Hello:

    def __init__(self):
        self.hello = "Ahoj, to jsem ja"
        self.novy = "Tak to je"
        pass

    def print_all(self):
        return " \ ".join([self.hello, self.novy])

    pass
