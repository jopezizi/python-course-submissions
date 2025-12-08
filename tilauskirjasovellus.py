class Tehtava:
    _seuraava__id = 1

    def __init__(self,kuvaus:str, koodari:str, tyomaara:str,):
        self.kuvaus = kuvaus
        self.tyomaara = int(tyomaara)
        self.koodari = koodari
        self.id = Tehtava._seuraava__id
        self.valmis = False
        Tehtava._seuraava__id += 1

    def __str__(self):
        ret = f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} "
        if self.on_valmis() == True:
            ret += "VALMIS"
        else:
            ret += "EI VALMIS"
        return ret
    
    def on_valmis(self):
        return self.valmis
    
    def merkkaa_valmiiksi(self):
        self.valmis = True

class Tilauskirja:
    def __init__(self):
        self.tilaukset = []

    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        self.tilaukset.append(Tehtava(kuvaus,koodari,tyomaara))

    def kaikki_tilaukset(self):
        return self.tilaukset
    
    def koodarit(self):
        koodarit =  [tilaus.koodari for tilaus in self.tilaukset]
        return list(set(koodarit))
    
    def merkkaa_valmiiksi(self, id:int):
        for tehtava in self.tilaukset:
            if tehtava.id == id:
                tehtava.merkkaa_valmiiksi()
                return
        raise ValueError


    def valmiit_tilaukset(self):
        return [tilaus for tilaus in self.tilaukset if tilaus.on_valmis()]
    
    def ei_valmiit_tilaukset(self):
        return [tilaus for tilaus in self.tilaukset if not tilaus.on_valmis()]
    
    def koodarin_status(self, koodari:str):
        if koodari not in self.koodarit():
            raise ValueError
        
        valmiit = [tilaus for tilaus in self.tilaukset if tilaus.koodari == koodari and tilaus.on_valmis()]
        ei_valmiit = [tilaus for tilaus in self.tilaukset if tilaus.koodari == koodari and not tilaus.on_valmis()]
        return (len(valmiit), len(ei_valmiit), sum([osa.tyomaara for osa in valmiit]), sum([osa.tyomaara for osa in ei_valmiit]))

class Tilauskirjasovellus:
    def __init__(self):
        self.__tilauskirja = Tilauskirja()

    def sovellus(self):
        print(f"komennot:\n0 lopetus\n1 lisää tilaus\n2 listaa valmiit\n3 listaa ei valmiit\n4 merkitse tehtävä valmiiksi\n5 koodarit\n6 koodarin status")
        while True:
            print()
            try:
                syote = int(input("komento: "))
                if syote == 0:
                    break
                elif syote == 1:
                    self.lisaa_tilaus()
                elif syote == 2:
                    self.listaa_valmiit()
                elif syote == 3:
                    self.listaa_ei_valmiit()
                elif syote == 4:
                    self.merkitse_valmiiksi()
                elif syote == 5:
                    self.koodarit()
                elif syote == 6:
                    self.koodarin_status()
                else:
                    self.virheilmoitus()
            except ValueError:
                self.virheilmoitus()
        
    def lisaa_tilaus(self):
        kuvaus = input("kuvaus: ")
        koodari_tyomaara = input("koodari ja työmääräarvio: ")
        osat = koodari_tyomaara.split(" ")
        if len(osat) != 2:
            self.virheilmoitus()
            return
        koodari = osat[0]
        tyomaara = osat[1]
        self.__tilauskirja.lisaa_tilaus(kuvaus,koodari,tyomaara)
        print("lisätty!")
    
    def listaa_valmiit(self):
        tilaukset = self.__tilauskirja.valmiit_tilaukset()
        if tilaukset:
            for tilaus in tilaukset:
                print(tilaus)
        else:
            print("ei valmiita")

    def listaa_ei_valmiit(self):
        tilaukset = self.__tilauskirja.ei_valmiit_tilaukset()
        if tilaukset:
            for tilaus in tilaukset:
                print(tilaus)
        else:
            print("kaikki valmista!")

    def merkitse_valmiiksi(self):
        id = int(input("tunniste: "))
        self.__tilauskirja.merkkaa_valmiiksi(id)
        print("merkitty valmiiksi")

    def koodarit(self):
        koodarilista = self.__tilauskirja.koodarit()
        if koodarilista:
            for koodari in koodarilista:
                print(koodari)
        
    def koodarin_status(self):
        koodari = input("koodari: ")
        tiedot = self.__tilauskirja.koodarin_status(koodari)
        print(f"työt: valmiina {tiedot[0]} ei valmiina {tiedot[1]}, tunteja: tehty {tiedot[2]} tekemättä {tiedot[3]}")

    def virheilmoitus(self):
        print("virheellinen syöte")


t = Tilauskirjasovellus()
t.sovellus()