import math

def tangent( x, y ):
    return 4*(math.exp(0.8*x))-(0.5*y)
     
def euler( x0, y0, h, x_stop ):
    y = y0
    x = x0
    while x < x_stop:
        y = y + h * tangent(x0, y)
        x = x + h
        print("x: " ,x, " y: ", "%.6f"% y)
 
    
x0 = 0
y0 = 2
h = 1
x_stop = 4
 
euler(x0, y0, h, x_stop)
