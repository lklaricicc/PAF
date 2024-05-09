import matplotlib.pyplot as plt
import numpy as np
import program as p

č1 = p.čestica (0.3,1,(0,0,0), (0.1,0.1,0.1), (0,0,0,), (0,0,1), 0.01)
č2 = p.čestica(0.3,-1, (0,0,0), (0.1,0.1,0.1), (0,0,0,), (0,0,1), 0.01)
pozitron = č1.gibanje (5)
elektron = č2.gibanje (5)

graf = plt.axes (projection = "3d")
graf.plot (elektron[:,0], elektron [:,1], elektron [:,2], label = "elektron")
graf.plot (pozitron [:,0], pozitron [:,1], pozitron[:,2], label = "pozitron")
graf.legend ()
plt.show ()

#tumač koordinata:
#0.3 je masa čestice, 1 odnosno -1 je naboj čestice, (0,0,0) je pozicija čestice u 3d prostoru (x,y,z), (0.1,0.1,0.1) je početna brzina čestice u 3d prostoru, (0,0,0) je električno polje u kojem se čestica nalazi 0 je jer ga ode nema, (0,0,1) je magnetsko polje u kojem se čestica nalazi i 0.01 je korak vremena za simulaciju gibanja
# u č1 je +1 zato što je ppozitivno nabijena, a u č2 je negativan jer je negativno nabijena čestica