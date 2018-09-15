import numpy as np
import matplotlib.pyplot as plt

'data building'
x=np.linspace(-5,5,20)
y=x**2
z=5*np.sin(x)


'plotting'

#plt figure is a good way to return and number (or name) separate figures
plt.figure(1)
#make plots
plt.plot(x,y,'k')
plt.plot(x,z,'b')

plt.figure(5)
plt.plot(x,z,'bo')

plt.figure('another plot')
plt.plot(x,y,'black',marker='^')