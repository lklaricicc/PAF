#euler kod za oba grafa

import matplotlib.pyplot as plt
import numpy as np
import program as pg

# Postavke čestica
masa = 0.3
naboj_elektron = -1
naboj_pozitron = 1
pozicija = (0, 0, 0)
brzina = (0.1, 0.1, 0.1)
elektricno_polje = (0, 0, 0)
magnetsko_polje = (0, 0, 1)
dt = 0.01
t = 5

# Kreiranje objekata čestica za Eulerovu metodu
elektron_euler = pg.čestica(masa, naboj_elektron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
pozitron_euler = pg.čestica(masa, naboj_pozitron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)

# Izračun putanja korištenjem Eulerove metode
putanja_euler_elektron = elektron_euler.gibanje_euler(t)
putanja_euler_pozitron = pozitron_euler.gibanje_euler(t)

# Prikazivanje rezultata u odvojenim grafovima
fig = plt.figure(figsize=(10, 8))

# Graf za Eulerovu metodu - Elektron
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(putanja_euler_elektron[:, 0], putanja_euler_elektron[:, 1], putanja_euler_elektron[:, 2], color = 'blue', label='Elektron (Euler)')
ax1.set_title('Elektron - Eulerova metoda')
ax1.legend()

# Graf za Eulerovu metodu - Pozitron
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(putanja_euler_pozitron[:, 0], putanja_euler_pozitron[:, 1], putanja_euler_pozitron[:, 2], color = 'orange', label='Pozitron (Euler)')
ax2.set_title('Pozitron - Eulerova metoda')
ax2.legend()

plt.tight_layout()
plt.show()
