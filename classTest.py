
class Zvire:

    def __init__(self, vek):
        print("Konstrukce zvirete")
        self.__vek = vek
        pass

    def get_vek(self):
        return self.__vek

    def set_vek(self, vek):
        self.__vek = vek
        pass

    def spat(self):
        raise NotImplementedError("The 'spat' method is not implemented")

    def jist(self):
        raise NotImplementedError("The 'jist' method is not implemented")

    def reprodukovat(self):
        raise NotImplementedError("The 'reprodukovat' method is not implemented")

    def pohybovat(self):
        raise NotImplementedError("The 'pohybovat' method is not implemented")

    def mluvit(self):
        raise NotImplementedError("The 'mluvit' method is not implemented")

    pass


class Savec(Zvire):

    def __init__(self, vek):
        super(Savec, self).__init__(vek=vek)
        print("Konstrukce savce")
        pass

    def reprodukovat(self):
        print("Reprodukce savce")
        pass

    pass


class PridavekSavce:

    def pridavek_srani(self):
        print("Savec sere jak o zivot")
        pass

    def pridavek_chcani(self):
        print("Savec chcije jak o zivot")
        pass

    pass


class Kun(Savec, PridavekSavce):

    def __init__(self, vek):
        super(Kun, self).__init__(vek=vek)
        print("Konstrukce Kone")
        pass

    def spat(self):
        print("Kun spi")

    def jist(self):
        print("Kun ji")

    def pohybovat(self):
        print("Kun cvala")

    def mluvit(self):
        print("Kun rehta: iahaaaaa")

    def pridavek_chcani(self):
        print("Kun chcije jak o zivot")

    def pridavek_srani(self):
        print("Kun sere koblihy jak o zivot")

    pass


class Pes(Savec, PridavekSavce):

    def __init__(self, vek, jmeno="Hola Hej"):
        super(Pes, self).__init__(vek=vek)
        self.__jmeno = jmeno
        print("Konstrukce Psa")
        pass

    @classmethod
    def extra_pes(cls):
        return cls(50, "Filko")

    def spat(self):
        print("Pes spi")

    def jist(self):
        print("Pes ji")

    def pohybovat(self):
        print("Pes poskakuje")

    def mluvit(self):
        print("Pes jmenem {} steka: haf haf haf".format(self.__jmeno))

    pass


class Zverinec:

    @staticmethod
    def predstaveni_zverince(mojeZvire = Zvire):
        print(type(mojeZvire))
        print(mojeZvire.get_vek())
        mojeZvire.spat()
        mojeZvire.jist()
        mojeZvire.reprodukovat()
        mojeZvire.pohybovat()
        mojeZvire.mluvit()
        print("++++++++++++++++++++++++++")
        pass

    @staticmethod
    def trosku_vice_zvirat(mojeZvire = PridavekSavce):
        mojeZvire.pridavek_chcani()
        mojeZvire.pridavek_srani()
        pass

    pass


if __name__ == '__main__':

    listZvirat = []
    listZvirat.append(Kun(vek=25))
    listZvirat.append(Pes(vek=28))
    listZvirat.append(Kun(vek=12))
    listZvirat.append(Pes.extra_pes())
    listZvirat.append(Kun(vek=48))
    listZvirat.append(Pes(vek=44))
    listZvirat.append(Pes(vek=68))

    for nejakeZvire in listZvirat:
        Zverinec.predstaveni_zverince(nejakeZvire)
        Zverinec.trosku_vice_zvirat(nejakeZvire)
        pass

    deleni, modulo = divmod(30, 12)
    print('30/12 je {} a zbytek {}'.format(deleni, modulo))
