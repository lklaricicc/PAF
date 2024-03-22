import numpy as np
import matplotlib.pyplot as plt
x= [1,2,3,4,5,6,7,8,9,10]
y= [11,12,13,14,15,16,17,18,19,20]

arth_x= np.mean(x)
arth_y= np.mean(y)
print(arth_x)
print(arth_y)

dev_x = np.std(x) / np.sqrt(len(x) - 1)
dev_y = np.std(y) / np.sqrt(len(y) - 1)
print(dev_x)
print(dev_y)

