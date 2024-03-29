import matplotlib.pyplot as plt
import numpy as np

class Particle: 
    def __init__(self,v0,fi,x0,y0, dt = 0.001): 
        self.v0=v0
        self.fi=fi
        self.x0=x0
        self.y0=y0
        self.dt = dt
        self.putx = []
        self.puty = []
        
        def info(self):                            
            print("v0:", self.v0)
            print("x0:", self.x0)
            print("y0:", self.y0)
            print("kut:", self.fi)
        
    def reset(self):                            
        self.v0 = 0
        self.y0 = 0
        self.x0 = 0
        self.fi = 0
        self.putx = []                          
        self.puty = []
        
    def __move(self, F, m, t):
        t0 = 0
        dt = 0.001
        g = 9.81
        vx0 = self.v0 * np.cos((self.fi/180)*np.pi)
        vy0 = self.v0 * np.sin ((self.fi /180)*np.pi)

        while t0 < t:
              self.x0 = self.x0 + vx0 *dt 
              self.putx.append (self.x0)
              vy = vy0 - g*dt 
              self.vy0 = vy 
              self.y0 = self.y0 +vy * dt 
              self.puty.append(self.y0)
              t0 = t0 + dt 

    def range(self):
        t = 0
        g = 9.81
        vx0 = self.v0 * np.cos ((self.fi /180) * np.pi)
        vy0 = self.v0 * np.sin ((self.fi /180) * np.pi)

        while self.y0 >= 0:
            self.x0 = self.x0 + vx0 * self.dt
            self.putx.append(self.x0)
            self.y0 = self.x0 + vy0 * self.dt
            self.puty.append(self.y0)

            vy0 = vy0 - g * self.dt

            t = t + self.dt

        self.x0 = self.putx [-1]
        self.y0 = 0
        return self.putx[-1]

    def plot_trajectory (self):
        self.range ()
        plt.xlabel ('x pozicija (m)')
        plt.ylabel ('y pozicija (m)')
        plt.title ('putanja čestice')
        plt.plot (self.putx, self.puty)
        plt.show ()
    
    def analiticki_domet(self):
        a_domet = ((self.v0)**2 * np.sin(2*((self.fi /180)*np.pi))) / 9.81
        return a_domet