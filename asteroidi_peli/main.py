import pygame, random
pygame.init()


class Teksti:
    def __init__(self):
        self.pisteet = 0

    def paivita(self,nollaus:bool):
        if nollaus:
            self.pisteet = 0
        else:
            self.pisteet += 1
    def teksti(self):
        fontti = pygame.font.SysFont("Arial", 24)
        teksti = fontti.render(f"Pisteet: {self.pisteet}",True,(255,0,0))
        naytto.blit(teksti, (naytto.get_width()-130,10))


class Asteroidi:
    def __init__(self):
        self.x = random.randint(0, naytto.get_width()-kivi.get_width())
        self.y = random.randint(-600,-50)

    def osuma(self,rx,ry):
        ax1 = self.x 
        ay1 = self.y
        ax2 = self.x + kivi.get_width()
        ay2 = self.y + kivi.get_height()

        rx1 = rx
        ry1 = ry
        rx2 = rx + robo.get_width()
        ry2 = ry + robo.get_height()

        return (ax1 < rx2 and ax2 > rx1 and ay1 < ry2 and ay2 > ry1)
    
    def tiputa(self):
        self.y += 1.5
        if self.y >= naytto.get_height():
            self.y= random.randint(-600,-50)
        naytto.blit(kivi,(self.x,self.y))

naytto = pygame.display.set_mode((640,480))
robo = pygame.image.load("src/robo.png")
kivi = pygame.image.load("src/kivi.png")
x=naytto.get_width()/2-robo.get_width()/2
y=naytto.get_height()-robo.get_height()
suunnat = {"v": False, "o": False}
kello = pygame.time.Clock()
teksti = Teksti()
pygame.display.set_caption("Asteroidit")
vaikeus = 5
asteroidit = [Asteroidi() for i in range (vaikeus)]


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                suunnat["v"] = True
            if tapahtuma.key == pygame.K_RIGHT:
                suunnat["o"] = True

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                suunnat["v"] = False
            if tapahtuma.key == pygame.K_RIGHT:
                suunnat["o"] = False

        if tapahtuma.type == pygame.QUIT:
            exit()
        
    if suunnat["v"]:
        x-=5
    if suunnat["o"]:
        x+=5
    
    x = max(x,0)
    x = min(x,naytto.get_width()-robo.get_width())

    naytto.fill((0,0,0))    
    naytto.blit(robo,(x,y))
    teksti.teksti()
    for a in asteroidit:
        a.tiputa()
        if a.osuma(x,y):
            teksti.paivita(False)
            a.y = random.randint(-600, -50)
        if a.y + kivi.get_height() >= naytto.get_height():
            teksti.paivita(True) #pelin päättyminen
            asteroidit = [Asteroidi() for i in range (vaikeus)] # nollataan asteroidit
            x=naytto.get_width()/2-robo.get_width()/2 # nollataan robo
            y=naytto.get_height()-robo.get_height()
    pygame.display.flip()
    kello.tick(60)
