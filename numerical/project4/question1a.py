
# Consider a differential equation
# dy / dx =(x + y + xy)
def func( x, y ):
    return (x + y + x * y)
     
# Function for euler formula
def euler( x0, y, h, x ):
    temp = -0
    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h
 
    print("Approximate solution at x = ", x, " is ", "%.6f"% y)
     
# Initial Values
x0 = 0
y0 = 1
h = 0.025
 
# Value of x at which we need approximation
x = 0.1
 
euler(x0, y0, h, x)
