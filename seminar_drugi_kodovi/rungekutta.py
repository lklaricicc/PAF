#rungekutta kod za dva grafa

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

# Kreiranje objekata čestica za Runge-Kutta metodu
elektron_rk4 = pg.čestica(masa, naboj_elektron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
pozitron_rk4 = pg.čestica(masa, naboj_pozitron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)

# Izračun putanja korištenjem Runge-Kutta metode
putanja_rk4_elektron = elektron_rk4.gibanje_rk4(t)
putanja_rk4_pozitron = pozitron_rk4.gibanje_rk4(t)

# Prikazivanje rezultata u odvojenim grafovima
fig = plt.figure(figsize=(10, 8))

# Graf za Runge-Kutta metodu - Elektron
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(putanja_rk4_elektron[:, 0], putanja_rk4_elektron[:, 1], putanja_rk4_elektron[:, 2], color = 'green', label='Elektron (RK4)')
ax1.set_title('Elektron - Runge-Kutta metoda')
ax1.legend()

# Graf za Runge-Kutta metodu - Pozitron
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(putanja_rk4_pozitron[:, 0], putanja_rk4_pozitron[:, 1], putanja_rk4_pozitron[:, 2], color = 'red',  label='Pozitron (RK4)')
ax2.set_title('Pozitron - Runge-Kutta metoda')
ax2.legend()

plt.tight_layout()
plt.show()
