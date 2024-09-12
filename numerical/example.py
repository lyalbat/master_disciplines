import numpy as np

xi = [0.6,0.4,0.5,0.2]

def jacobian(Ca):
    a = [-1.4048-0.3334*Ca,0.8333,0,-1.6667]
    b = [0,-2.2381,1.6667,0]
    c = [0,0,-0.5714,0]
    d = [0,0,0,-0.5714]
    return [a,b,c,d]

def original_func(xi):
    a = (-1)*(5.7143-1.4048*xi[0]-0.1667*(xi[0]**2))
    b = (-1)*(0.8333*xi[0]-2.2381*xi[1])
    c = (-1)*(1.6667*xi[1] - 0.5714*xi[2])
    d = (-1)*(0.0833*(xi[0]**2)-0.5714*xi[3])
    return [a,b,c,d]

def crammer(det,dx1,dx2,dx3,dx4):
    x1 = dx1/det
    x2 = dx2/det
    x3 = dx3/det
    x4 = dx4/det
    return [x1,x2,x3,x4]

def determinant(matrix):
    #print('the matrix: ',matrix)
    A = np.array(matrix)
    det = np.linalg.det(A) 
    #print('the determinant: ', det)
    return det

def calculate_xi(delta,xi_minus):
    xi = []
    for i in range(len(delta)):
        a = delta[i] - xi_minus[i]
        xi.append(a)
    return xi

def calculate_error(xi,xi_minus):
    error = []
    for i in range(len(xi)):
        a = abs((xi[i] - xi_minus[i])/xi_minus[i])*100
        error.append(a)
    return error

ea = 0.005
error = 100
while error>ea:
    j = jacobian(xi[0])
    f = original_func(xi)
    det = determinant(j)
    dx1 = determinant([f,j[1],j[2],j[3]])
    print('dx1: ',dx1)
    dx2 = determinant([j[0],f,j[2],j[3]])
    print('dx2: ',dx2)
    dx3 = determinant([j[0],j[1],f,j[3]])
    print('dx3: ',dx3)
    dx4 = determinant([j[0],j[1],j[2],f])
    print('dx4: ',dx4)
    delta = crammer(det,dx1,dx2,dx3,dx4)
    xi_minus = xi
    print('xi-1: ', xi_minus)
    xi = calculate_xi(delta,xi_minus)
    print('xi: ', xi)
    et = calculate_error(xi,xi_minus)
    print('error: ', et)
    error = et[0]
    print('-------- fim da iteracao-------')