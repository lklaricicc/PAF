import matplotlib.pyplot as plt
import numpy as np
class Particle:
    def __init__(self, fi, v0, x0, y0, dt = 0.001):
        self.fi = fi
        self.v0 = v0
        self.x0 = x0
        self.y0 = v0
        self.dt = dt
        self.koox = []
        self.kooy = []

    def info(self):
        print("kut otklona:", self.fi)
        print("v0", self.v0)
        print("x0:", self.x0)
        print("y0:", self.y0)
    
    def reset(self):
        self.fi = 0
        self.v0 = 0
        self.x0 = 0
        self.y0 = 0
        self.koox = []
        self.kooy = []
    
    def __move(self,F,m,t):
        t0 = 0
        dt = 0.001
        g = 9.81
        vx0 = self.v0 * np.cos ((self.fi/180) * np.pi)
        vy0 = self.v0 * np.sin ((self.fi / 180) * np.pi)

        while t0 < t:
            self.x0 = self.x0 + vx0 * dt
            self.koox.append(self.x0)
            vy = vy0 - g * dt
            self.vy0 = vy
            self.y0 = self.y0 + vy * dt
            self.kooy.append(self.y0)

    def range(self):
        t = 0
        g = 9.81
        vx0 = self.v0 * np.cos ((self.fi / 180) * np.pi)
        vy0 = self.v0 * np.sin ((self.fi /180) * np.pi)

        while self.y0 >= 0:
            self.x0 = self.x0 + vx0 * self.dt
            self.koox.append(self.x0)
            self.y0 = self.y0 + vy0 * self.dt
            self.kooy.append(self.y0)
            vy0 = vy0 - g * self.dt
            t = t + self.dt
        
        self.x0 = self.koox[-1]
        self.y0 = 0
        return self.koox[-1]
    
    def plot_trajectory(self):
        plt.plot (self.koox,self.kooy)
        plt.show ()
    def analiticki_domet(self):
        domet = ((self.v0) ** 2 * np.sin (2 * (self.fi / 180) * np.pi)) / 9.81
        return domet