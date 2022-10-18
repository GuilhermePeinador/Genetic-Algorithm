import numpy as np
from numpy import arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

def func (x,y):
    return  x + y + (0.5) * (x ** 2 + y ** 2 - 2)**2

x = np.arange(-1.0,1.0,0.1)
y = np.arange(-1.0,1.0,0.1)
X,Y = meshgrid(x,y)
Z = func(X,Y)

im = imshow(Z,cmap=cm.RdBu) # drawing the function

cset = contour(Z,arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10) #adding the Contour lines with labels

colorbar(im) # adding the colobar on the right

# latex fashion title
title('$z = x + y + 0.5(x^2 + y^2 - 2)^2 $')
show()
