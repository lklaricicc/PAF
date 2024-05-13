import matplotlib.pyplot as plt
import numpy as np

# Početni uvjeti
q = -1.602e-19  # Električni naboj elektrona u Coulombima
m = 9.109e-31  # Masa elektrona u kg
E = [100, 0, 0]  # Električno polje (V/m), samo u x smjeru
B = [0, 0, 1]  # Magnetno polje (T), samo u z smjeru
v0 = [1e5, 1e5, 0]  # Početna brzina (m/s), u x i y smjeru
dt = 1e-9  # Korak vremena za simulaciju (s)
T = 1e-5  # Trajanje simulacije (s)

class nabijena_cestica: 
    def __init__ (self,q,m,E,B,v0,dt):
        self.q = q
        self.m = m
        self.E = np.array (E)
        self.B = np.array (B)
        self.v = np.array (v0)
        self.dt = dt
        self.r = np.array ([0,0,0 ])
        self.gibanje = [self.r.copy()]

    def euler(self, T):
        t = 0
        while t < T:
            # Računanje ubrzanja čestice
            a = (self.q / self.m) * (self.E + np.cross(self.v, self.B))
            # Ažuriranje brzine i položaja čestice
            self.v = self.v + a * self.dt
            self.r = self.r + self.v * self.dt
            # Dodavanje novog položaja u listu
            self.gibanje.append(self.r.copy())
            t += self.dt

    def plot_gibanje(self):
        gibanje = np.array(self.gibanje)
        plt.plot(gibanje[:, 0], gibanje[:, 1])
        plt.xlabel('X pozicija')
        plt.ylabel('Y pozicija')
        plt.title('Putanja nabijene čestice')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

graf = plt.axes (projection = "3d")
cestica = nabijena_cestica (q,m,E,B,v0,dt)
cestica.plot_gibanje ()
