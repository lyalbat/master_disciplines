import math

from numpy import *
import matplotlib.pyplot as plt

#funcao da derivada no ponto xi, yi
def tangent(x,y):
    return 4*math.exp(0.8*x)-(0.5*y)

#passo escolhido
h = 1

#valores iniciais
x = [0]
y = [2]

for i in range(1,5,h):
    x_before = x[i-1]
    y_before = y[i-1]

    #metodo de euler
    y_now = y_before + tangent(x_before,y_before)*h
    x_now = x_before + h

    x.append(x_now)
    y.append(y_now)

print("x: ", x)
print("y: ", y)

y_heun = [2,6.7010819,16.3197819,37.1992489,83.3377674]
y_analytical = [2,6.1946314,14.8439219,33.6771718,75.3389626]

plt.plot(x, y_analytical, 'r') # plotting t, a separately 
plt.plot(x, y_heun, 'b') # plotting t, b separately 
lineObjects = plt.plot(x, y, 'g') # plotting t, c separately 
plt.legend(['Resultado Analitico', 'Metodo Heun', 'Metodo Euler'])
plt.show()
