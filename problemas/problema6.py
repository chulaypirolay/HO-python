import numpy as np
import matplotlib.pyplot as pp

tabla = np.loadtxt("tabla.txt",delimiter=" ") 

x=tabla[:,0]
y=tabla[:,1]

pp.plot(x, y, color='r', label='x vs. y')

pp.show()