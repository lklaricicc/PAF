import matplotlib.pyplot as plt
import numpy as np

class čestica: #definiram klasu čestica koja modelira svojstva i ponašanja čestice čije gibanje opisujem
    def __init__(self,m,q,s,v,E,B,dt):#def __init__ definira se kao konstruktor klase čestica, on inicijalizira objekt sa zadanim parametrima
        #zadani parametri: masa m, naboj q, pozicija s, brzina v, električno polje E, magnetsko polje B, vrijeme izraženo kao dt
        self.m = m
        self.q = q 
        #self.m = m i self.q = q su atributi objekta na predane vrijednosti
        self.s = np.array(s)
        self.v = np.array(v)
        self.E = np.array (E)
        self.B = np.array (B)
        self.dt = dt
    
    def gibanje (self, t): #definiram metodu gibanje koja simulira gibanje čestice u vremenskom intervalu t
        t0 = 0 #vrijeme namještam na nulu
        putanja = [] #stvaram praznu listu putanja gdje se sadržavaju pozicije čestice tijekom vremena
        vrijeme = np.arange (t0,t,self.dt) #generira se niz vremenskih koraka od t0 do t s korakom dt
        for i in vrijeme: #petlja prolazi kroz svaki taj vremenski korak
            a = (self.q/self.m) * (self.E + (np.cross (self.v, self.B))) #ubrzanje čestice koristeći Lorentzovu silu
            self.v = self.v + a * self.dt #računanje brzine čestice 
            self.s = self.s + self.v * self.dt #računanje pozicije čestice
            putanja.append (self.s) #dodaje se nova pozicija čestice u listu trajanja
        return np.array (putanja) 