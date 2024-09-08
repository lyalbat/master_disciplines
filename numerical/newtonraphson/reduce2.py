import numpy as np

def reduceTo3b3(matrix,refPosition=0):
    smaller = []
    for i in range(len(matrix[refPosition])):
        small = []
        for l in range(len(matrix)):
            if(l == 0):
                pass
            else:
                line = matrix[l]
                for col in range(len(line)):
                    if(col== i):
                        pass
                    else:
                        small.append(line[col])
        smaller.append(small)
    return smaller

l1 = [1,0,4,-6]
l2 = [2,5,0,3]
l3 = [-1,2,3,5]
l4 = [2,1,-2,3]
big = [l1,l2,l3,l4]
matrix3 = reduceTo3b3(big,0)
for i in range(len(matrix3)):
    newarr = np.array_split(matrix3[i], 3)
    print(newarr)