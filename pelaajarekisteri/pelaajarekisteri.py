import json

class Pelaaja:
    def __init__(self,tiedot):
        self.name = tiedot["name"]
        self.nationality = tiedot["nationality"]
        self.assists = tiedot["assists"]
        self.goals = tiedot["goals"]
        self.penalties = tiedot["penalties"]
        self.team = tiedot["team"]
        self.games = tiedot["games"]



class Pelaajatiedot:
    def __init__(self, tiedosto):
        with open(tiedosto,"r") as j:
            raakatiedot = json.load(j)
        self.pelaajalista = [Pelaaja(p) for p in raakatiedot]

    def tulosta_tiedot(self, nimi):
        for pelaaja in self.pelaajalista:
            if pelaaja.name == nimi:
                print(f"{pelaaja.name:<21}{pelaaja.team:<3}  {pelaaja.goals:>2} + {pelaaja.assists:>2} = {pelaaja.goals + pelaaja.assists:>3}")


        
    def tulosta_joukkueet(self):
        j = sorted(list(set([p.team for p in self.pelaajalista])))
        for t in j:
            print(t)

    def tulosta_maat(self):
        m = sorted(list(set([p.nationality for p in self.pelaajalista])))
        for n in m:
            print(n)

    def tulosta_joukkue(self, joukkue):
        def eniten(pelaaja: Pelaaja):
            return pelaaja.goals + pelaaja.assists
        j = sorted([p for p in self.pelaajalista if p.team == joukkue],key=eniten,reverse=True)
        print()
        for pelaaja in j:
            print(f"{pelaaja.name:<21}{pelaaja.team:<3}  {pelaaja.goals:>2} + {pelaaja.assists:>2} = {pelaaja.goals + pelaaja.assists:>3}")


    def tulosta_maa(self, maa):
        def eniten(pelaaja: Pelaaja):
            return pelaaja.goals + pelaaja.assists
        m = sorted([p for p in self.pelaajalista if p.nationality == maa],key=eniten,reverse=True)
        print()
        for pelaaja in m:
            print(f"{pelaaja.name:<21}{pelaaja.team:<3}  {pelaaja.goals:>2} + {pelaaja.assists:>2} = {pelaaja.goals + pelaaja.assists:>3}")




    def eniten_pisteita(self, monta):

        eniten = sorted([p for p in self.pelaajalista],key=lambda t:(-(t.goals+t.assists), t.games))
        print()
        for pelaaja in eniten[:monta]:
            print(f"{pelaaja.name:<21}{pelaaja.team:<3}  {pelaaja.goals:>2} + {pelaaja.assists:>2} = {pelaaja.goals + pelaaja.assists:>3}")




    def eniten_maaleja(self, monta):

        eniten = sorted([p for p in self.pelaajalista],key=lambda t:(-(t.goals), t.games))
        print()
        for pelaaja in eniten[:monta]:
            print(f"{pelaaja.name:<21}{pelaaja.team:<3}  {pelaaja.goals:>2} + {pelaaja.assists:>2} = {pelaaja.goals + pelaaja.assists:>3}")



def main():
    tiedosto = input("tiedosto: ")
    try:
        tiedot = Pelaajatiedot(tiedosto)
    except:
        print("Virheellinen tiedosto")
        return
    
    print(f"luettiin {len(tiedot.pelaajalista)} pelaajan tiedot")
    
    print('''\nkomennot:
0 lopeta
1 hae pelaaja
2 joukkueet
3 maat
4 joukkueen pelaajat
5 maan pelaajat
6 eniten pisteitä
7 eniten maaleja''')
    while True:
        print()
        kom = int(input("komento: "))

        if kom == 0:
            break

        elif kom == 1:
            nimi = input("nimi: ")
            tiedot.tulosta_tiedot(nimi)

        elif kom == 2:
            tiedot.tulosta_joukkueet()
        
        elif kom == 3:
            tiedot.tulosta_maat()

        elif kom == 4:
            joukkue = input("joukkue: ")
            tiedot.tulosta_joukkue(joukkue)

        elif kom == 5:
            maa = input("maa: ")
            tiedot.tulosta_maa(maa)

        elif kom == 6:
            monta = int(input("kuinka monta: "))
            tiedot.eniten_pisteita(monta)

        elif kom == 7:
            monta = int(input("kuinka monta: "))
            tiedot.eniten_maaleja(monta)
main()
