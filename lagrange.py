import numpy as np
import matplotlib.pyplot as plt

def lag(x, y, num):
    """
    'num' is a set of given points, use x and y to figure out lagrange
    polynomial and calculate all the corresponding values for num

    Implement as you wish but your 'total' numpy array
    has to return all the results 
    """

    assert(len(x)==len(y))
    total  = np.zeros(len(num))

    #place your code here!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(len(num)):
        total[i] = lagPol(num[i], x, y)

    return total

def lagPol(xi, x, y):
    res = 0
    for i in range(len(x)):
        res += y[i]*lagCoeff(xi, i, x)
    return res

def lagCoeff(xi, i, x):
    res = 1
    for j in range(len(x)):
        if(j != i):
            res *= (xi-x[j])/(x[i]-x[j])
    return res
    
data_x = np.array([-3.,-2.,-1.,0.,1.,3.,4.])
data_y = np.array([-60.,-80.,6.,1.,45.,30.,16.])
# data_x = np.array([10.,15.,20.,22.5])
# data_y = np.array([227.4,362.78,517.35,602.97])

#generating 50 points from -3 to 4 in order to create a smooth line
X = np.linspace(-3, 4, 50, endpoint=True)
F = lag(data_x, data_y, X)
print(F)
plt.plot(X,F)
plt.plot(data_x, data_y, 'ro')
plt.show()