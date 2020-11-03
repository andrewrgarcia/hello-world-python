import numpy as np
import matplotlib.pyplot as plt

'data building'
x=np.linspace(-5,5,20)
y=x**2
z=5*np.sin(x)


'plotting'
#make plots

#plt figure is a good way to return and number (or name) separate figures
plt.figure(2)
plt.plot(x,y,'k',label = 'black')
plt.plot(x,z,'b',label = 'blue')
plt.legend(title='line colors')

plt.figure(4)
plt.plot(x,z,'bo')

plt.xlabel(r'$\phi$  /  $\infty$')
plt.ylabel('${E^2}\div{c^4}$  /  $kg^2$  ')

plt.figure('Another Figure')
plt.title('Title here')
plt.plot(x,y,'black',marker='^')
plt.xlabel('x')
plt.ylabel('y')
