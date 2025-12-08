class Sarja:
    def __init__(self, nimi:str, kaudet:int, genret:list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvosanat = []
    
    def arvostele(self, arvosana: int):
        if arvosana >= 0 and arvosana <= 5:
            self.arvosanat.append(arvosana)

    def __str__(self):
        tuloste = f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: "
        for i in range(len(self.genret)):
            tuloste+=f"{self.genret[i]}, "
        tuloste = tuloste.rstrip(", ")
        if len(self.arvosanat) > 0:
            keskiarvo = sum(self.arvosanat) / len(self.arvosanat)
            tuloste += f"\narvosteluja {len(self.arvosanat)}, keskiarvo {keskiarvo:.1f} pistettä"
        else:
            tuloste += "\nei arvosteluja"
        return(tuloste)



def arvosana_vahintaan(arvosana: float, sarjat: list):
    sopivat = []
    for sarja in sarjat:
        keskiarvo = sum(sarja.arvosanat)/len(sarja.arvosanat)
        if keskiarvo >= arvosana:
            sopivat.append(sarja)
    return sopivat

def sisaltaa_genren(genre: str, sarjat: list):
    sopivat = []
    for sarja in sarjat:
        for yks_genre in sarja.genret:
            if genre.lower()==yks_genre.lower():
                sopivat.append(sarja)
                break
    return sopivat
