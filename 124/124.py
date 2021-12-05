import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def give_pos_ellipse_coord(a,b):
	x=np.arange(-a,1001/1000*a,a/100000)
	y1=np.sqrt((1-(x/a)**2)*b**2)
	return y1

"""
a=0.352
b=0.312
x_max=0.55
y_max=0.55
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(231)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_x$, у.е.")
plt.ylabel(r"$I_y$, у.е.")
plt.axis([-x_max,x_max,-y_max,y_max])
a=0.511
b=0.312
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(232)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_z$, у.е.")
plt.ylabel(r"$I_y$, у.е.")
plt.axis([-x_max,x_max,-y_max,y_max])
a=0.352
b=0.511
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(233)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_x$, у.е.")
plt.ylabel(r"$I_z$, у.е.")
plt.axis([-x_max,x_max,-y_max,y_max])



a=0.609
b=0.602
x_max=0.65
y_max=0.65
sp=plt.subplot(234)
x=np.arange(-a,1001/1000*a,a/100000)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_x$, у.е.")
plt.ylabel(r"$I_y$, у.е.")
plt.axis([-x_max,x_max,-y_max,y_max])
a=0.609
b=0.602
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(235)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_z$, у.е.")
plt.ylabel(r"$I_y$, у.е.")
plt.axis([-x_max,x_max,-y_max,y_max])
a=0.609
b=0.609
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(236)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_x$, у.е.")
plt.ylabel(r"$I_z$, у.е.")
plt.axis([-x_max,x_max,-y_max,y_max])

"""
x_max=0.65
y_max=0.65
a=0.595
b=0.409
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(121)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_x$, у.е.")
plt.ylabel(r"$I_y$, у.е.")
plt.title("Цилиндр 1")
plt.axis([-x_max,x_max,-y_max,y_max])


a=0.194
b=0.214
x_max=0.25
y_max=0.25
x=np.arange(-a,1001/1000*a,a/100000)
sp=plt.subplot(122)
plt.plot(x, give_pos_ellipse_coord(a,b), 'b', x, -1*give_pos_ellipse_coord(a,b), 'b' )
plt.xlabel(r"$I_x$, у.е.")
plt.ylabel(r"$I_y$, у.е.")
plt.title("Цилиндр 2")
plt.axis([-x_max,x_max,-y_max,y_max])
plt.show()
