import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(v0, t, ukupno_vrijeme):
    v0 = 25
    x = v0 * t
    plt.plot(t, x, label='Jednoliko gibanje')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj x (m)')
    plt.legend()
    plt.grid(True)

def kosi_hitac(v0, theta, t):
    g = 9.81
    x = v0 * np.cos(np.radians(theta)) * t
    y = v0 * np.sin(np.radians(theta)) * t - 0.5 * g * t**2
    plt.plot(x, y, label='Kosi hitac')
    plt.xlabel('Položaj x (m)')
    plt.ylabel('Položaj y (m)')
    plt.legend()
    plt.grid(True)
