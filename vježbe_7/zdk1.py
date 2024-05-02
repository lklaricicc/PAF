import matplotlib.pyplot as plt
import numpy as np
import Projectile as pro

t1 = pro.Projectile(0.11,0,0,10,0.1,0.1,0.1,45)
a,b = t1.Euler()
plt.plot(a,b)
plt.show()