import numpy as np
import matplotlib.pyplot as plt

M = [0.052,0.124,0.168,0.236,0.284,0.336]
fi = [0.1745,0.3491,0.5236,0.6981,0.8727,1.0472]
#y os je M, a x os fi, definiramo dvije liste kao u zdk 3

suma_M = sum(M)    #suma (svih elemenata liste)
suma_fi = sum(fi)

arth_M = suma_M/len(M)  #aritmetička sredina
arth_fi = suma_fi/len(fi)

a = arth_M*arth_fi/arth_fi**2 #prema zadanoj formuli računamo koeficijent 
b = 0
m = []
for element in fi: #za svaki element izračunavamo F
    F = a * element 
    m.append(F) #m je prazna lista u koju pohranjujemo rezultate 
    
sigma = np.sqrt((1/len(M) * ((arth_M**2/arth_fi**2)-a**2))) 
#koristimo formulu za izračun standardne devijacije koeficijenta a kojeg smo izrazili kao sigmu
#sigma daje informaciju o stabilnosti i pouzdanosti procjene koeficijenta a
print("a =", a) #ispisujemo a 
plt.scatter (fi, M) #pokazuje raspršene podatke
plt.plot (fi, m) #prikazuje linearni model
plt.title ("D = {} +/- {}".format(round(a,9), round(sigma, 9))) #naslov grafa
plt.show()
