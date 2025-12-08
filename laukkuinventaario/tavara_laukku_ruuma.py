# Tee ratkaisusi tähän:
class Tavara:
    def __init__(self, nimi, paino):
        self.__nimi=nimi
        self.__paino=paino

    def __str__(self):
        return(f"{self.__nimi} ({self.__paino} kg)")
    
    def nimi(self):
        return self.__nimi
    
    def paino(self):
        return self.__paino
    


class Matkalaukku:
    def __init__(self, maxpaino:int):
        self.__maxpaino = maxpaino
        self.__matkalaukku = []
        self.__yhtpaino = 0


    def __str__(self):
        pituus = len(self.__matkalaukku)
        if pituus == 1:
            return(f"1 tavara ({self.__yhtpaino} kg)")
        else:
            return(f"{pituus} tavaraa ({self.__yhtpaino} kg)")

    def lisaa_tavara(self, tavara):
        tavpaino = tavara.paino()
        if tavpaino+self.__yhtpaino <= self.__maxpaino:
            self.__matkalaukku.append(tavara)
            self.__yhtpaino += tavpaino

    def tulosta_tavarat(self):
        for tavara in self.__matkalaukku:
            print(tavara)

    def paino(self):
        return self.__yhtpaino
    
    def raskain_tavara(self):
        if len(self.__matkalaukku) == 0:
            return None
        raskain = self.__matkalaukku[0]
        for tavara in self.__matkalaukku:
            paino = tavara.paino()
            if paino > raskain.paino():
                raskain = tavara
        return raskain


class Lastiruuma:
    def __init__(self, maxpaino:int):
        self.__maxpaino= maxpaino
        self.__lastiruuma = []
        self.__yhtpaino = 0

    def lisaa_matkalaukku(self, matkalaukku):
        laukkupaino = matkalaukku.paino()
        if laukkupaino + self.__yhtpaino <= self.__maxpaino:
            self.__lastiruuma.append(matkalaukku)
            self.__yhtpaino += matkalaukku.paino()

    def __str__(self):
        pituus = len(self.__lastiruuma)
        if pituus == 1:
            return(f"{pituus} matkalaukku, tilaa {self.__maxpaino-self.__yhtpaino} kg")
        else:
            return(f"{pituus} matkalaukkua, tilaa {self.__maxpaino-self.__yhtpaino} kg")
    def tulosta_tavarat(self):
        for matkalaukku in self.__lastiruuma:
            matkalaukku.tulosta_tavarat()
