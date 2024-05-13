import matplotlib.pyplot as plt
import numpy as np

m1 = 1.989 * 10**30  # masa Sunca
m2 = 5.9742 * 10**24  # masa Zemlje
r1 = np.array([0, 0])  # početni položaj Sunca
r2 = np.array([1.486 * 10**11, 0])  # početni položaj Zemlje
v1 = np.array([0, 0])  # početna brzina Sunca
v2 = np.array([0, 29783])  # početna brzina Zemlje
dt = 86400  # korak vremena u sekundama (jedan dan)
trajanje_dana = 365.242  # trajanje simulacije u danima
G = 6.67408 * 10**-11  # gravitacijska konstanta


def gravitacijska_sila (r,m1,m2,G): #definiram funkciju gravitacijska_sila koja računa grav.silu između 2 čestice; funkcija prima poziciju r između čestica mase m1 i m2, a G je gravitacijska konstanta
    r_norm = np.linalg.norm(r) #
    return -G * m1 * m2 / r_norm **3 * r #vraćanje rezultata, izračunavanje grav sile prema N.z.

def putanja (m1,m2,r1,r2,v1,v2,dt, trajanje_dana, G): #definiram funkciju putanja koja simulira kretanje čestica, ona primas+ mase, poč.položaje, poč brzine, korak vremena, trajanje gibanja i grav konst
    trajanje_sekunde = trajanje_dana * 24 * 3600 #pretvaram trajanje gibanja simulacije iz dana u sekunde jer je vrijeme u sekundama
    č1 = [np.array(r1)] #inicijalizira se lista za pohranu položaja prve čestice 
    č2 = [np.array(r2)] #inicijalizira se lista za pohranu položaja druge čestice 
    
    t = 0
    while t < trajanje_sekunde: #petlja koja traje dok simulacija ne dostigne zadano trajanje
        r = np.array(r2) - np.array(r1) #računanje vektora relativnog položaja dvije čestice
        
        a1 = gravitacijska_sila(r, m1, m2, G) / m1 #izračunavanje akceleracije prve čestice 
        v1 = v1 + a1 * dt #ažuriranje brzine koristeći Eulerovu metodu
        r1 = r1 + v1 * dt #ažuriranje položaja koristeći ažuriranu brzinu
        č1.append(r1.copy()) #dodavanje trenutnog položaja prve čestice koristeći novu (ažuriranu) brzinu

        a2 = gravitacijska_sila(-r, m2, m1, G) / m2 #ista stvar za česticu 2
        v2 = v2 + a2 * dt
        r2 = r2 + v2 * dt
        č2.append(r2.copy())

        t += dt #ažuriranje vremena simulacije za korak vremena

    return np.array(č1), np.array(č2) #vraćanje rezultata simulacije kao nizova položaja čestica

putanja_sunca, putanja_zemlje = putanja(m1, m2, r1, r2, v1, v2, dt, trajanje_dana, G) #postavljanje početnih uvjeta, pozivanje funkcije putanja i prikaz rezultata

# prikaz rezultata
plt.plot(putanja_zemlje[:, 0], putanja_zemlje[:, 1], label='Zemlja')
plt.scatter(putanja_sunca[-1, 0], putanja_sunca[-1, 1], color='yellow', label='Sunce')
plt.xlabel('X pozicija (m)')
plt.ylabel('Y pozicija (m)')
plt.title('Putanja Zemlje oko Sunca')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()