import numpy as np
import matplotlib.pyplot as plt

#x returns 20 evenly spaced numbers b/t -5 and 5 as a vector
x=np.linspace(-5,5,20)

y=x**2

plt.plot(x,y)