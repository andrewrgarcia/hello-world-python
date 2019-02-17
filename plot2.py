'''loads numpy (numerical python) package; makes vector operations (line 9)
and other numerical features possible '''
import numpy as np
import matplotlib.pyplot as plt


#create a vector with the following numbers in sequence
x=np.array([-5,2,3,4,5])
#y returns vector of operated x vector (operation y = x^2)
y=x**2

plt.plot(x,y)