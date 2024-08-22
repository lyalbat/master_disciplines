pressure = [0.1,5,10,30,50]
coldestTempEntalpy = [200,4.1,2.2,0.9,0.54]
mediumTempEntalpy = [250,4.7,2.5,0.99,0.6]
hottestTempEntalpy = [282.5,5.23,2.7,1.03,0.62]

FlowData = [4,4.25,4.9,5.1,4.6,4.3,4.7,5.1]
ConcentrationData = [10,17,38,54,40,37,36,33]
t = [0,5,15,25,35,40,45,55]

def customFunc(x):
    return FlowData[x]*ConcentrationData[x]

def trapeziumMethod(a,b):
    h = b - a
    x0 = t.index(a)
    x1 = t.index(b)
    func = (customFunc(x0)+customFunc(x1))/2
    return h * func

def simpson13Method(a,b,c):
    '''if(c != (a+b)/2):
        return "Invalid data for this method"
        '''
    x0 = t.index(a)
    x1 = t.index(b)
    x2 = t.index(c)
    h = (c-a)/2
    func = (customFunc(x0)+4*customFunc(x1)+customFunc(x2))/3
    return h * func

def simpson38Method(a,b,c,d):
    x0 = t.index(a)
    x1 = t.index(b)
    x2 = t.index(c)
    x3 = t.index(d)
    h = (d-a)
    func = (customFunc(x0)+3*customFunc(x1)+3*customFunc(x2)+customFunc(x3))/8
    return h * func



integral_1 = trapeziumMethod(0,5)
print(integral_1)
integral_2 = simpson38Method(5,15,25,35)
print(integral_2)
integral_3= simpson13Method(35,40,45)
print(integral_3)
integral_4 = trapeziumMethod(45,55)
print(integral_4)
integral= integral_1 + integral_2 + integral_3 + integral_4

print(integral)
