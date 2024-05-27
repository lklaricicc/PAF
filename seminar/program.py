#dio iz vježbe 8 i početni file koji se u sve ostale primjere importa 
import numpy as np

class čestica:
    def __init__(self, m, q, p, v, E, B, dt):
        self.m = m
        self.q = q
        self.p = np.array(p, dtype=float)
        self.v = np.array(v, dtype=float)
        self.E = np.array(E, dtype=float)
        self.B = np.array(B, dtype=float)
        self.dt = dt

    def gibanje_euler(self, t):
        t0 = 0
        putanja = []
        vrijeme = np.arange(t0, t, self.dt)
        for _ in vrijeme:
            a = (self.q / self.m) * (self.E + np.cross(self.v, self.B))
            self.v = self.v + a * self.dt
            self.p = self.p + self.v * self.dt
            putanja.append(self.p.copy())
        return np.array(putanja)
    
    def gibanje_rk4(self, t):
        t0 = 0
        putanja = []
        vrijeme = np.arange(t0, t, self.dt)
        for _ in vrijeme:
            p1, v1 = self.p, self.v
            a1 = (self.q / self.m) * (self.E + np.cross(v1, self.B))
            
            p2, v2 = self.p + 0.5 * self.dt * v1, self.v + 0.5 * self.dt * a1
            a2 = (self.q / self.m) * (self.E + np.cross(v2, self.B))
            
            p3, v3 = self.p + 0.5 * self.dt * v2, self.v + 0.5 * self.dt * a2
            a3 = (self.q / self.m) * (self.E + np.cross(v3, self.B))
            
            p4, v4 = self.p + self.dt * v3, self.v + self.dt * a3
            a4 = (self.q / self.m) * (self.E + np.cross(v4, self.B))
            
            self.p = self.p + (self.dt / 6.0) * (v1 + 2 * v2 + 2 * v3 + v4)
            self.v = self.v + (self.dt / 6.0) * (a1 + 2 * a2 + 2 * a3 + a4)
            
            putanja.append(self.p.copy())
        return np.array(putanja)
