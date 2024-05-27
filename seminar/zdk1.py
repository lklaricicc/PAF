import matplotlib.pyplot as plt
import numpy as np
import program as pg

# Postavke čestica
masa = 0.3
naboj_elektrona = -1
pozicija = (0, 0, 0)
brzina = (0.1, 0.1, 0.1)
elektricno_polje = (0, 0, 0)
magnetsko_polje = (0, 0, 1)
dt = 0.01
t = 5

# Kreiranje objekata čestica
elektron_euler = pg.čestica(masa, naboj_elektrona, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
# Izračun putanja korištenjem Eulerove metode
putanja_elektron_euler = elektron_euler.gibanje_euler(t)

# Resetiranje početnih uvjeta za Runge-Kutta metodu
elektron_rk4 = pg.čestica(masa, naboj_elektrona, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
# Izračun putanja korištenjem Runge-Kutta metode
putanja_elektron_rk4 = elektron_rk4.gibanje_rk4(t)

# Prikazivanje rezultata u odvojenim grafovima
fig = plt.figure(figsize=(12, 10))

# Graf za Eulerovu metodu - Čestica
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(putanja_elektron_euler[:, 0], putanja_elektron_euler[:, 1], putanja_elektron_euler[:, 2], color='blue', label='Elektron (Euler)')
ax1.set_title('Eulerova metoda')
ax1.legend()

# Graf za Runge-Kutta metodu - Čestica
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(putanja_elektron_rk4[:, 0], putanja_elektron_rk4[:, 1], putanja_elektron_rk4[:, 2], color='green', label='Elektron (RK4)')
ax2.set_title('Runge-Kutta metoda')
ax2.legend()

plt.subplots_adjust(hspace=0.5)
plt.tight_layout()
plt.show()
