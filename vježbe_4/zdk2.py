import matplotlib.pyplot as plt
import numpy as np
import particle as part

t = 0.001
vrijeme = []
error = []
while t<=0.1:
    p = part.Particle (10,60,0,0,t)
    err = (np.abs(p.range() - p.analiticki_domet())/p.analiticki_domet())*100
    error.append(err)
    t = t+ 0.001
    vrijeme.append (t)
plt.plot (vrijeme,error)
plt.show ()