import matplotlib.pyplot as plt
import numpy as np
import program as pg

č1 = pg.čestica (0.3,1,(0,0,0), (0.1,0.1,0.1), (0,0,0,), (0,0,1), 0.01)
č2 = pg.čestica(0.3,-1, (0,0,0), (0.1,0.1,0.1), (0,0,0,), (0,0,1), 0.01)
pozitron = č1.gibanje (5) #simuliram gibanje čestice tijekom 5 vremenskih koraka
elektron = č2.gibanje (5)

graf = plt.axes (projection = "3d") #stvaram 3d graf za prikaz putanje čestice
for putanja, ime in zip([elektron, pozitron], ["elektron", "pozitron"]):
    graf.plot(putanja[:, 0], putanja[:, 1], putanja[:, 2], label=ime)
graf.legend ()
plt.show ()

#tumač koordinata:
#0.3 je masa čestice (proizvoljno uzeta), 1 odnosno -1 je naboj čestice, (0,0,0) je pozicija čestice u 3d prostoru (x,y,z), (0.1,0.1,0.1) je početna brzina čestice u 3d prostoru, (0,0,0) je električno polje u kojem se čestica nalazi 0 je jer ga ode nema, (0,0,1) je magnetsko polje u kojem se čestica nalazi i 0.01 je korak vremena za simulaciju gibanja
#ostale veličine su uzete iz prezentacije sa predavanja
#u č1 je +1 zato što je pozitivno nabijena, a u č2 je negativan jer je negativno nabijena čestica
#č1 i č2 su objekti tipa čestica sa zadanim parametrima

#alternativa za liniju 10 i 11 u kojima su koordinate za x,y,z u zagradama:
#graf.plot (elektron [:,0], elektron [:,1], elektron[:,2], label = "elektron")
#graf.plot (pozitron [:,0], pozitron [:,1], pozitron [:,2], label = "pozitron")