class OpRekisteriSovellus:
    def __init__(self):
        self.__rekisteri = Opintorekisteri()
    def suorita(self):
        while True:
            print("")
            print("1 lisää suoritus")
            print("2 hae suoritus")
            print("3 tilastot")
            print("0 lopetus\n")
            
            komento=int(input("komento: "))
            if komento == 1:
                self.lisaa_suoritus()
            elif komento == 2:
                self.hae_suoritus()
            elif komento == 3:
                self.tilastot()
            elif komento == 0:
                break
            else:
                print("")
                continue
    
    def lisaa_suoritus(self):
        kurssi = input("kurssi: ")
        arvosana = input("arvosana: ")
        opintopisteet = input("opintopisteet: ")
        self.__rekisteri.lisaa_suoritus(kurssi, arvosana, opintopisteet)

    def hae_suoritus(self):
        kurssi = input("kurssi: ")
        self.__rekisteri.hae_suoritus(kurssi)

    def tilastot(self):
        pass


class Opintorekisteri:
    def __init__(self):
        self.__merkinnat = {}

    def lisaa_suoritus(self, kurssi:str, arvosana:str, opintopisteet:str):
        nyk_kurssi = self.__merkinnat[kurssi]
        if not nyk_kurssi:
            self.__merkinnat[kurssi]={"arvosana":arvosana, "opintopisteet":opintopisteet}
        else:
            if nyk_kurssi[arvosana] 
    
    def hae_suoritus(self, kurssi:str):
        tiedot = self.__merkinnat[kurssi]
        arvosana = tiedot["arvosana"]
        opintopisteet = tiedot["opintopisteet"]
        print(f"{kurssi} ({opintopisteet} op) arvosana {arvosana}")


sovellus = OpRekisteriSovellus()
sovellus.suorita()