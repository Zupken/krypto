from time import sleep
from random import randrange
from string import ascii_lowercase


class Odbiorca:

    def krok_pierwszy(self):
        self.p = 29
        self.g = randrange(1, self.p)
        self.b = randrange(1, self.p)
        self.B = self.g ** self.b % self.p
        self.public_key = {'p': self.p, 'g': self.g, 'B': self.B}
        
    def krok_drugi(self):
        #Wyslij klucz publiczny do nadawcy
        Nadawca.public_key = self.public_key

    def krok_piaty(self):
        self.c = self.zaszyfrowana_wiadomosc['c']
        self.A = self.zaszyfrowana_wiadomosc['A']
        self.K = self.A**self.b % self.p
        
        for m in range(0, self.p):
            if (m* self.K) % self.p == self.c:
                break
        print(chr(96+m))


class Nadawca:

    def __init__(self):
        self.m = 0

    def krok_zerowy(self, m):
        self.m = ascii_lowercase.index(m)+1
        
    def krok_trzeci(self):
        self.p = self.public_key['p']
        self.g = self.public_key['g']
        self.B = self.public_key['B']
        
        self.a = randrange(1, self.p)
        
        self.A = self.g ** self.a % self.p
        self.c = self.m*(self.B**self.a) % self.p

    def krok_czwarty(self):
        self.zaszyfrowana_wiadomosc = {'c': self.c, 'A': self.A}
        Odbiorca.zaszyfrowana_wiadomosc = self.zaszyfrowana_wiadomosc


wiadomosc = input("Podaj wiadomosc ktora chcesz wyslac: ")

Nadawca = Nadawca()
Odbiorca = Odbiorca()
for c in wiadomosc:
    Nadawca.krok_zerowy(c)
    Odbiorca.krok_pierwszy()
    Odbiorca.krok_drugi()
    Nadawca.krok_trzeci()
    Nadawca.krok_czwarty()
    Odbiorca.krok_piaty()





