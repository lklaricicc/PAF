import matplotlib.pyplot as plt
import numpy as np

def derivacija (funkcija,x,h,korak = 3):
    if korak == 3:
        print ((funkcija(x+h)-funkcija(x-h)) / (2*h))
    if korak == 2:
        return (funkcija(x+h)-funkcija(x)) / h
    else:
        raise ValueError ("Neispravna metoda, odaberite trokorak ili dvokorak.")

def derivacija_u_rasponu (funkcija, donja_granica, gornja_granica,h,korak = 3):
   tocke = []
   iznosi = []
   while donja_granica <= gornja_granica:
       tocke.append(donja_granica)
       if korak == 3:
           iznosi.append(derivacija(funkcija,donja_granica,h,korak))
       elif korak == 2:
           iznosi.append((funkcija(donja_granica + h) - funkcija (donja_granica)) /h)
           donja_granica += h
           return tocke,iznosi

def integral (funkcija,donja_granica,gornja_granica,h):
    tocke = []
    donji_integral = []
    gornji_integral = []
    donja_suma = 0
    gornja_suma = 0
    while donja_granica <= gornja_granica:
        tocke.append(donja_granica)
        donja_suma += funkcija (donja_granica) * h
        donji_integral.append (donja_suma)
        donja_granica += h
        tocke.append(donja_granica)
        gornja_suma += funkcija (donja_granica) * h
        gornji_integral.append(gornja_suma)
        donja_granica += h
    return tocke,donji_integral, tocke [1:], gornji_integral

def trapezno_pravilo (funkcija, donja_granica, gornja_granica, koraci):
    h = (gornja_granica - donja_granica) / koraci
    donja_suma = 0
    gornja_suma = 0
    prosjecna_suma = 0
    i = 0
    while i < koraci:
        donja_suma += funkcija(donja_granica) * h
        gornja_suma += funkcija(donja_granica + h) *h
        prosjecna_suma += ((h/2) * (funkcija(donja_granica) + funkcija(donja_granica+h)))
        donja_granica += h
        i += 1
    return donja_suma,gornja_suma,prosjecna_suma 
