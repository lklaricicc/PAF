import matplotlib.pyplot as plt
import numpy as np

class čestica: #definiram klasu čestica koja modelira vrijednosti i ponašanja čestice čije gibanje opisujem
    def __init__(self,m,q,p,v,E,B,dt):#def __init__ definira se kao konstruktor klase čestica, on inicijalizira objekt sa zadanim parametrima
        #zadani parametri: masa m, naboj q, pozicija p, brzina v, električno polje E, magnetsko polje B, vrijeme izraženo kao dt
        self.m = m
        self.q = q 
        #self.m = m i self.q = q su atributi objekta na zadane vrijednosti, u prijveodu postavljam m ili q unutar tog objekta na neku vrijednost m ili q koju sam definirala
        self.p = np.array(p)
        self.v = np.array(v)
        self.E = np.array (E)
        self.B = np.array (B)
        self.dt = dt
        #ove linije koda omogućuju "čestici" da zna koje su njegove karakteristike 
    
    def gibanje (self, t): #definiram metodu gibanje koja simulira gibanje čestice u vremenskom intervalu t
        t0 = 0 #vrijeme namještam na nulu
        putanja = [] #stvaram praznu listu putanja gdje se sadržavaju pozicije čestice tijekom vremena
        vrijeme = np.arange (t0,t,self.dt) #generira se niz vremenskih koraka od t0 do t s korakom dt
        for i in vrijeme: #petlja prolazi kroz svaki taj vremenski korak
            a = (self.q/self.m) * (self.E + (np.cross (self.v, self.B))) #ubrzanje čestice koristeći Lorentzovu silu
            self.v = self.v + a * self.dt #računanje brzine čestice 
            self.p = self.p + self.v * self.dt #računanje pozicije čestice
            putanja.append (self.p) #dodaje se nova pozicija čestice u listu trajanja
        return np.array (putanja) 