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
        print("p = {}\ng = {}\nb = {}\nB = {}\n".format(self.p, self.g, self.b, self.B))
        input()
        
    def krok_drugi(self):
        #Wyslij klucz publiczny do nadawcy
        Nadawca.public_key = self.public_key
        print("Klucz publiczny = ", Nadawca.public_key)
        input()

    def krok_piaty(self):
        self.c = self.zaszyfrowana_wiadomosc['c']
        self.A = self.zaszyfrowana_wiadomosc['A']
        self.K = self.A**self.b % self.p

        print("K = ", self.K)
        input()
        
        for m in range(1, self.p):
            print("m = {} wartosc wyrazenia wynosi {}".format(m, (m* self.K) % self.p), end="")
            input()
            if (m* self.K) % self.p == self.c:
                print("Poprawna wartosc m to: ",m)
                break
        
        print("Zaszyfrowany znak to: ",chr(96+m))
        input()


class Nadawca:

    def __init__(self):
        self.m = 0

    def krok_zerowy(self, m):
        self.m = ascii_lowercase.index(m)+1
        print("m =", self.m)
        input()
        
    def krok_trzeci(self):
        self.p = self.public_key['p']
        self.g = self.public_key['g']
        self.B = self.public_key['B']
        
        self.a = randrange(1, self.p)
        
        self.A = self.g ** self.a % self.p
        self.c = self.m*(self.B**self.a) % self.p

        print("a = {}\nA = {}\nc = {} \n".format(self.a, self.A, self.c))
        self.zaszyfrowana_wiadomosc = {'c': self.c, 'A': self.A}
        input()

    def krok_czwarty(self):
        Odbiorca.zaszyfrowana_wiadomosc = self.zaszyfrowana_wiadomosc
        print('Zaszyfrowana wiadomosc: ', Odbiorca.zaszyfrowana_wiadomosc)
        input()


wiadomosc = input("Podaj wiadomosc ktora chcesz wyslac: ")

Nadawca = Nadawca()
Odbiorca = Odbiorca()
i=1
for c in wiadomosc:
    print("Litera numer ",i, "czyli litera: ",c)
    Nadawca.krok_zerowy(c)
    Odbiorca.krok_pierwszy()
    Odbiorca.krok_drugi()
    Nadawca.krok_trzeci()
    Nadawca.krok_czwarty()
    Odbiorca.krok_piaty()
    i += 1





