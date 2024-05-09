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