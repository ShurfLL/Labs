import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math



m=np.array([39.42, 37.11, 11.80])/1000
d=np.array([1.20, 1.22, 1.17])/100
l=np.array([39.7, 41.3, 40.1])/1000
po=m/np.pi/d**2*4/l


#print(np.average(mfr))

#print(w)
#print (np.std(w
n=np.array([1,2,3])
fm=np.array([3251.7,6465.2,9755.0])
p, v = np.polyfit(n, fm, deg=1, cov=True)
p_f = np.poly1d(p)
k1=p[0]
x = np.arange(0, 3, 0.01)
sp=plt.subplot(221)
plt.plot(n, fm, '.', x, p_f(x))
plt.title("медь")
plt.xlabel("$n$")
plt.ylabel("$f, Гц$")
plt.grid()
fs=np.array([4117.6,8235.4,12354.9])
p, v = np.polyfit(n, fs, deg=1, cov=True)
p_f = np.poly1d(p)
k2=p[0]
x = np.arange(0, 3, 0.01)
sp=plt.subplot(222)
plt.plot(n, fs, '.', x, p_f(x))
plt.title("сталь")
plt.xlabel("$n$")
plt.ylabel("$f, Гц$")
plt.grid()
fd=np.array([4261.4,8521.2,12785.1])
p, v = np.polyfit(n, fd, deg=1, cov=True)
p_f = np.poly1d(p)
k3=p[0]
x = np.arange(0, 3, 0.01)
sp=plt.subplot(223)
plt.plot(n, fd, '.', x, p_f(x))
plt.title("дюраль")
plt.xlabel("$n$")
plt.ylabel("$f, Гц$")
plt.grid()
plt.show()
u=np.array([3251, 4118, 4261])*2*0.6
E=po*u**2/1000000000
fn1=np.array([3251, 4118, 4261])

sigu=2*0.6/math.sqrt(3)*math.sqrt(-(-(np.average(fd**2))/(np.average(n**2))+4261**2))
sigE=E*sigu/u
print(sigu)
print(np.average(fm))

