import matplotlib.pyplot as plt
import numpy as np
from zdk1.py import calculus 

def f2(x):
    return x**2

koraci = []
gornje_granice = []
donje_granice = []
prosjecne = []

for i in range (100,900,100):
    a,b,c = calculus.trapezno_pravilo (f2,0,1,i)
    koraci.append (a)
    donje_granice.append (b)
    gornje_granice.append (c)

plt.scatter (koraci, donje_granice, c = "blue")
plt.scatter (koraci, gornje_granice, c = "red")
plt.plot (koraci,prosjecne,c = "green")
plt.show ()