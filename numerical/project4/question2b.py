
def func1( y ):
    return (-0.5)*y
def func2( y1, y2 ):
    return 4-(0.3*y2)-(0.1*y1)
     
def euler( x0, y01, y02, h, stop_x ):
    y1 = y01
    y2 = y02
    x = x0
    while x != stop_x:
        tmp_y1 = y1
        y1 = y1 + h * func1(y1)
        y2 = y2 + h * func2(tmp_y1,y2)
        x = x + h
        print("Approximate solution at x = ", x, " is y1: ", "%.6f"% y1, "and y2: ", "%.6f"% y2)
 
     
# Valores iniciais
x0 = 0
y01 = 4
y02 = 6
h = 0.5
 
# Valor de x ate o fim da aproximacao
stop_x = 2
 
euler(x0, y01, y02, h, stop_x)
