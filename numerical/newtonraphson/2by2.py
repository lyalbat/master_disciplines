#funcao para calcular determinante de matriz 2x2

l1 = [3,5]
l2 = [-2,3]
A = [l1,l2]
det1 = 1
det2 = 1
const = 5
for l in range(len(A)):
    line = A[l]
    for col in range(len(line)):
        element = line[col]
        if l == col:
            det1 = det1 * element
        else:
            det2 = det2 * element
        print("linha: "+ str(l) + " col: " + str(col) + " valor: " + str(element))
determ = const * (det1 - det2)
print("det1: " + str(det1)+ "+ det2: " + str(det2) + " = " + str(determ))