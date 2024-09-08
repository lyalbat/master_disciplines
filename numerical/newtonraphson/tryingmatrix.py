l1 = [1,0,4,-6]
l2 = [2,5,0,3]
l3 = [-1,2,3,5]
l4 = [2,1,-2,3]
A = [l1,l2,l3,l4]
ref = []
#percorre a matriz
for l in range(len(A)):
    line = A[l]
    for col in range(len(line)):
        print("linha: "+ str(l) + " col: " + str(col) + " valor: " + str(line[col]))