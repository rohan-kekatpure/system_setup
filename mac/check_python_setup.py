import numpy as np
import scipy as sp
import matplotlib.pylab as pl
import sklearn as skl

x = np.random.random((100, ))
y = np.sin(x)
pl.plot(x, y, 'ro')
pl.show()

# I'll enhance the script as we progress.