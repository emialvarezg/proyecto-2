#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#función para simular una caminata aleatoria en dZ^2
def caminata(p,n,d=1):
  x0=0
  y0=0
  x=[x0]
  y=[y0]
  for i in range(n):
    if np.random.uniform() < p:
      x0 += 1
    else:
      x0 -= 1
    
    if np.random.uniform() < p:
      y0 += 1
    else:
      y0 -= 1

    x.append(d*x0)
    y.append(d*y0)
    
  return x,y

#función para borrar los ciclos de un camino 
def borrar_ciclos(x,y):
  lx = []
  ly = []
  while 0 < len(x):
    #print(x,y)
    #encontramos el máximo índice en el que aparece el punto (x,y)
    ind = [i for i in range(len(x)) if x[0] == x[i] and y[0] == y[i]]
    lx.append(x[max(ind)])
    ly.append(y[max(ind)])
    #nos quedamos con los puntos de la caminata que están despues del índice encontrado
    m = max(ind) + 1
    x = x[m:]
    y = y[m:]
    #print('x',x,y)
    #print('lx',lx,ly)
  return lx,ly


# In[3]:


#función para cortar un camino cuando sale del disco de radio r por primera vez
def tA(x,y,r):
  for i in range(1,len(x)):
    if np.sqrt(x[i-1]**2 + y[i-1]**2) < r and  np.sqrt(x[i]**2 + y[i]**2) >= r:
      return x[:i+1],y[:i+1]
      break


# In[98]:


#para graficar un círculo
l1 = np.linspace(-0.25,1,200)
l2 = np.sqrt(1-l1**2)
l3 = -np.sqrt(1-l1**2)


# In[110]:


#ejemplo
x,y=caminata(1/2,10000,0.1)


# In[111]:


plt.plot(x,y)
#plt.scatter(x,y,color = 'k')


# In[35]:


lx,ly = borrar_ciclos(x,y)


# In[36]:


plt.plot(x,y)
plt.plot(lx,ly)
plt.scatter([x[0],x[-1]],[y[0],y[-1]],color='r')


# In[95]:


x2,y2 = tA(x,y,1)
lx2,ly2 = borrar_ciclos(x2,y2)
#x3,y3 = tA(x,y,5)
#lx3,ly3 = borrar_ciclos(x3,y3)


# In[99]:


plt.plot(l1,l2,color='k')
#plt.plot(l1,l3,color='k')
plt.plot(x2,y2,label='X[0,t_A]')
plt.plot(lx2,ly2,label='L^A')
#plt.scatter([x[0],x[-1]],[y[0],y[-1]],color='r')
#plt.plot(lx2,ly2,color='r')
#plt.plot(lx3,ly3,color='g')
plt.legend()


# In[100]:


tA(lx2,ly2,1) == tA(lx3,ly3,1)


# In[177]:


plt.plot(l1,l2,color='k')
plt.plot(l1,l3,color='k')
#plt.plot(x,y)
#plt.plot(lx,ly,color='r')
#plt.scatter([x[0],x[-1]],[y[0],y[-1]],color='r')
plt.plot(lx2,ly2,color='r')


# In[41]:


#gráfica para ejemplo de camino con ciclos borrados
xej = [0,1,2,2,1,1,1,2]
yej = [0,0,0,1,1,0,-1,-1]
lxej = [0,1,1,2]
lyej = [0,0,-1,-1]
plt.plot(xej,yej,label='x')
plt.plot(lxej,lyej,color='r',label='L(x)')
plt.scatter(xej,yej,color='k')
plt.legend()


