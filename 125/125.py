import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def sigmasluch(x):
    return ("\sigma^{сл}_"+x+"= \sqrt{\frac{1}{N - 1} \sum_{i = 1}^{N} \left("+x+"_i -\langle "+x+" \rangle \right)^2}")


def srkv(X):
     s=0
     for x in X:
          s+=(x-np.average(X))^2
     return s



def sluch(X):
     sig=math.sqrt((1/(X.size()-1))*(srkv(X)))
     return sig


m=np.array([341.2, 273.6, 219.2, 178.5, 141.2, 116.4, 92.8])
M=m*9.8/1000*0.12
T=np.array([30.3, 154/4, 143/3, 144/2.5, 145/2, 180/2, 166/1.5])
Omega=2*np.pi/T


M=np.round(M,2)
Omega=np.round(Omega,2)

print(Omega)

data=[M, Omega]
index=["$M, H\cdot m$", "$\Omega,c^{-1}$"]
columns=[i for i in range (1,8)]
df=pd.DataFrame(data, index, columns)
with open('125', 'w') as tf:
     tf.write(df.to_latex())

p, v = np.polyfit(M, Omega, deg=1, cov=True)
p_f = np.poly1d(p)
x = np.arange(0.1, 0.4, 0.001)
plt.plot(M, Omega, '.', x, p_f(x))
plt.xlabel("$M, H\cdot m$")
plt.ylabel("$\Omega,c^{-1}$")
plt.grid()
plt.show()


t1=np.array([3.138, 3.155, 3.195])
t2=np.array([4.084,4.000,4.034])
t1=np.append(t1,np.average(t1))
t2=np.append(t2,np.average(t2))
t1=np.round(t1,3)
t2=np.round(t2,3)
data=[t1,t2]
index=["$T_0$", "$T_1$"]
columns=[1, 2, 3, "$T_ср$"]
df=pd.DataFrame(data, index, columns)
with open('125_1', 'w') as tf:
     tf.write(df.to_latex())
I=0.00076
w=M/I/Omega

data=[M, w]
index=["$M, H\cdot m$", "$\omega,c^{-1}$"]
columns=[i for i in range (1,8)]
df=pd.DataFrame(data, index, columns)
with open('125_2', 'w') as tf:
     tf.write(df.to_latex())

t=np.array([151, 154, 143, 144, 145, 180, 166])
data=[t]
index = ["$t,c$"]
columns = [i for i in range (1,8)]
df=pd.DataFrame(data, index, columns)
with open('125_3', 'w') as tf:
     tf.write(df.to_latex())
Omegafr = 2*np.pi/t
mfr= 0.0008*Omegafr*w
print(mfr)


print(np.average(mfr))

print(w)
print (np.std(w))