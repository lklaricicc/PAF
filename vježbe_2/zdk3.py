import kinematika as kin
import matplotlib.pyplot as plt
import numpy as np

# definiram parametre po stoti put koristim v0_jednoliko etc da mi je lakše razlikovati koji parametar je za što
v0_jednoliko = 25
t_jednoliko = np.linspace(0, 10, 100)  # vremenska os od 0 do 10 sekundi s "korakom" 0.1,
#, 0 je poč vr niza, 10 je krajnja, a 100 ili 0.1 je broj točaka koje generiraju 100 jednako razmaknutih vr unutar raspona od 0 do 10

v0_kosi_hitac = 25
theta = 53
t_kosi_hitac = np.linspace(0, 10, 100) 

# pravim subplot s jednim retkom i pet stupaca
plt.figure(figsize=(15, 5))

# jednoliko gibanje (x-t graf)
plt.subplot(1, 5, 3)
kin.jednoliko_gibanje(v0_jednoliko, t_jednoliko, 10)
plt.title('x-t graf')

# prvi prazni podgraf
plt.subplot(1, 5, 1)
plt.axis('off')

# kosi hitac (x-y graf)
plt.subplot(1, 5, 2)
kin.kosi_hitac(v0_kosi_hitac, theta, t_kosi_hitac)
plt.title('x-y graf')

# kosi hitac (y-t graf)
plt.subplot(1, 5, 4)
kin.kosi_hitac(v0_kosi_hitac, theta, t_kosi_hitac)
plt.title('y-t graf')

# drugi prazni podgraf
plt.subplot(1, 5, 5)
plt.axis('off')

plt.tight_layout()  # naredba kojom sprječavam preklapanje grafova
plt.show()

