import matplotlib.pyplot as plt
import numpy as np

def kosi_hitac(v0, theta, vrijeme_koraka, ukupno_vrijeme):
    g = 9.81
    theta_rad = np.radians(theta)

    x, y, vx, vy = 0.0, 0.0, v0 * np.cos(theta_rad), v0 * np.sin(theta_rad)
    lista_t, lista_x, lista_y = [], [], []

    for t in np.arange(0, ukupno_vrijeme + vrijeme_koraka, vrijeme_koraka):
        ax, ay = 0.0, -g

        vx += ax * vrijeme_koraka
        vy += ay * vrijeme_koraka

        x += vx * vrijeme_koraka
        y += vy * vrijeme_koraka

        lista_t.append(t)
        lista_x.append(x)
        lista_y.append(y)

    return lista_t, lista_x, lista_y

def crtaj_grafove(lista_t, lista_x, lista_y):
    plt.plot(lista_x, lista_y, label='x-y Graf')
    plt.xlabel('Položaj x (m)')
    plt.ylabel('Položaj y (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(lista_t, lista_x, label='x-t Graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj x (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(lista_t, lista_y, label='y-t Graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj y (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

v0 = 25 
theta = 53
vrijeme_koraka = 1 
ukupno_vrijeme = 10

t, x, y = kosi_hitac(v0, theta, vrijeme_koraka, ukupno_vrijeme)
crtaj_grafove(t, x, y)

