import matplotlib.plyot as plt
import numpy as np

def jednoliko_gibanje (v0,t):
    x = v0*t
    plt.plot(t,x,label='Jednoliko gibanje')
    plt.show ()

def kosi_hitac(v0, theta, t):
    g =9.81
    x = v0*np.cos(np.radians(theta))*t
    y = v0*np.sin(np.radians(theta))*t - o.5*g*t**2
    plt.plot(x,y,label='Kosi hitac')
    plt.show()