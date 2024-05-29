#oba koda u jednom ali s odvojenim grafovima na finalnom prikazu

import matplotlib.pyplot as plt
import numpy as np
import program as pg

# Postavke čestica
masa = 0.3
naboj_elektron = -1
naboj_pozitron = 1
pozicija = (0, 0, 0) #čestica započinje iz ishodišta koo.sus.
brzina = (0.1, 0.1, 0.1) #stavljene su vrijednosti različite od nule kako bi čestica reairala na magnetskom polje u 3d
elektricno_polje = (0, 0, 0) #stavljeno je na nulu jer želimo proučavati gibanje čestice samo u magnetskom polju
magnetsko_polje = (0, 0, 1) #u zdk u vježbi 8 definirano je kao 0,0,B što znači da je usmjereno put z osi i mi ćemo postaviti B na 1
dt = 0.01
t = 5

# Kreiranje objekata čestica
elektron_euler = pg.čestica(masa, naboj_elektron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
pozitron_euler = pg.čestica(masa, naboj_pozitron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)

# Izračun putanja korištenjem Eulerove metode
putanja_euler_elektron = elektron_euler.gibanje_euler(t)
putanja_euler_pozitron = pozitron_euler.gibanje_euler(t)

# Resetiranje početnih uvjeta za Runge-Kutta metodu
elektron_rk4 = pg.čestica(masa, naboj_elektron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)
pozitron_rk4 = pg.čestica(masa, naboj_pozitron, pozicija, brzina, elektricno_polje, magnetsko_polje, dt)

# Izračun putanja korištenjem Runge-Kutta metode
putanja_rk4_elektron = elektron_rk4.gibanje_rk4(t)
putanja_rk4_pozitron = pozitron_rk4.gibanje_rk4(t)

# Prikazivanje rezultata u odvojenim grafovima
fig = plt.figure(figsize=(12, 10))

# Graf za Eulerovu metodu - Elektron
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot(putanja_euler_elektron[:, 0], putanja_euler_elektron[:, 1], putanja_euler_elektron[:, 2], color = 'blue', label='Elektron (Euler)')
ax1.set_title('Elektron - Eulerova metoda')
ax1.legend()

# Graf za Eulerovu metodu - Pozitron
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot(putanja_euler_pozitron[:, 0], putanja_euler_pozitron[:, 1], putanja_euler_pozitron[:, 2], color = 'orange',label='Pozitron (Euler)')
ax2.set_title('Pozitron - Eulerova metoda')
ax2.legend()

# Graf za Runge-Kutta metodu - Elektron
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot(putanja_rk4_elektron[:, 0], putanja_rk4_elektron[:, 1], putanja_rk4_elektron[:, 2], color = 'green', label='Elektron (RK4)')
ax3.set_title('Elektron - Runge-Kutta metoda')
ax3.legend()

# Graf za Runge-Kutta metodu - Pozitron
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot(putanja_rk4_pozitron[:, 0], putanja_rk4_pozitron[:, 1], putanja_rk4_pozitron[:, 2], color = 'red', label='Pozitron (RK4)')
ax4.set_title('Pozitron - Runge-Kutta metoda')
ax4.legend()

plt.subplots_adjust (hspace = 0.5)


plt.tight_layout()
plt.show()
