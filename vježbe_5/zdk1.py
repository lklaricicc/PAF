import matplotlib.pyplot as plt
import numpy as np
import calculus as cls

def f1(x):
    return x**3

cls.derivacija(f1,2,0.01)
a,b = cls.derivacija (f1, -2,2,0.1)
c,d = cls.derivacija (f1,-2,2,0.01)
plt.scatter (a,b,s = 2, c= "red")
plt.plot (c,d)
plt.show()
