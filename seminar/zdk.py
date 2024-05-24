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

# Kreiranje objekata čestica
elektron = pg.čestica(masa, naboj_elektron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
pozitron = pg.čestica(masa, naboj_pozitron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)

# Izračun putanja korištenjem Eulerove metode
putanja_euler_elektron = elektron.gibanje_euler(t)
putanja_euler_pozitron = pozitron.gibanje_euler(t)

# Resetiranje početnih uvjeta
elektron = pg.čestica(masa, naboj_elektron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
pozitron = pg.čestica(masa, naboj_pozitron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)

# Izračun putanja korištenjem Runge-Kutta metode
putanja_rk4_elektron = elektron.gibanje_rk4(t)
putanja_rk4_pozitron = pozitron.gibanje_rk4(t)

# Prikazivanje rezultata
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Eulerova metoda
ax.plot(putanja_euler_elektron[:, 0], putanja_euler_elektron[:, 1], putanja_euler_elektron[:, 2], color = 'blue',label='Elektron (Euler)')
ax.plot(putanja_euler_pozitron[:, 0], putanja_euler_pozitron[:, 1], putanja_euler_pozitron[:, 2], color = 'red' ,label='Pozitron (Euler)')

# Runge-Kutta metoda
ax.plot(putanja_rk4_elektron[:, 0], putanja_rk4_elektron[:, 1], putanja_rk4_elektron[:, 2], color = 'green', label='Elektron (RK4)')
ax.plot(putanja_rk4_pozitron[:, 0], putanja_rk4_pozitron[:, 1], putanja_rk4_pozitron[:, 2], color = 'black', label='Pozitron (RK4)')

ax.legend()
plt.show()
