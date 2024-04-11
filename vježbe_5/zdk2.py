import matplotlib.pyplot as plt
import numpy as np
import calculus as cls

def f2(x):
    return x**2

koraci = []
gornje_granice = []
donje_granice = []
prosjecne = []

for i in range (100,900,100):
    a,b,c = cls.trapezno_pravilo (f2,0,1,i)
    koraci.append (i)
    donje_granice.append (a)
    gornje_granice.append (b)
    prosjecne.append (c)

plt.scatter (koraci, donje_granice, c = "pink")
plt.scatter (koraci, gornje_granice, c = "pink")
plt.scatter (koraci,prosjecne, c = "purple")
plt.plot (koraci,prosjecne,c = "black")
plt.show ()