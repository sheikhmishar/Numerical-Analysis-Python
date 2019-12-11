# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    
    def __init__(self, coefficients):
        '''
        This class implements a polynomial function.
        It takes input the coefficients of a n-order polynomial as a list
        and given m number of inputs X, it returns the corresponding Y.
        
        usage:
        p = Polynomial([a_0, a_1, ..., a_n])
        X = np.linspace(-3, 3, 50, endpoint=True)
        F = p(X)
        plt.plot(X,F)
        '''
        
        self.coefficients = coefficients
    
    def __repr__(self):
        '''
        method to return the canonical string representation 
        of a polynomial.
   
        '''
        return "Polynomial" + str(self.coefficients)
    
    def __call__(self, x):
        '''
        This method calculates the ordinate (Y-axis) given the 
        abscissa (X-axis) of a particular point on the polynomial.
        
        input: x can be a number or a numpy array
        '''
        
        # Initialize return value
        res = 0

        # Calculate the y_i given x_i
        # remember: y_i = f(x_i)
        # y_i = a_0 + a_1 * x_i ^ 1 + a_2 * x_i ^ 2 + ... + a_n * x_i ^ n
        #
        # use a for loop to calculate res
        # your loop might look like this
        for index, coeff in enumerate(self.coefficients):
            res += coeff*(x**index)
        
        return res
    
    def degree(self):
        return len(self.coefficients)
    
    def __str__(self):
        res = ""
        res += str(self.coefficients[0])
        for i in range(1, len(self.coefficients)):
            coeff = self.coefficients[i]
            if coeff < 0:
                res += " - " +  str(-coeff) + "x^" + str(i)
            else:
                res += " + " +  str(coeff) + "x^" + str(i)
        
        return res


def get_coefficients(x, y):
    '''
    Given a set of Xs and Ys, this function tries to form a 
    Vandermonde matrix. It then uses np.linalg.pinv to find the
    inverse of the matrix to calculate the coefficients of the 
    n-order polynomial to fit the given data points.
    
    usage:
    x = np.array([0,1,2])
    y = np.array([0,1,4])
    coefficients = get_coefficients(x, y) # array([-0.,  0.,  1.])
                                          # y = f(x) = 0 + 0 + x^2
    '''

    # Get length
    length = len(x)
    
    # Create (len X len) matrix
    coeff = np.zeros((length, length))
    
    # Populate the matrix
    
    # a_0 + a_1 * x_0 + a_2 * x_0^2 + .. a_n * x_0^n = y_0
    # a_0 + a_1 * x_1 + a_2 * x_1^2 + .. a_n * x_1^n = y_1
    # a_0 + a_1 * x_2 + a_2 * x_2^2 + .. a_n * x_2^n = y_2
    # .. .. ..
    # a_0 + a_1 * x_(n-1) + a_2 * x_(n-1)^2 + .. a_n * x_(n-1)^n = y_(n-1)
    
    # |1  x_0     x_0^2     ... x_0^n    | |a_0|   |  y_0  |
    # |1  x_1     x_1^2     ... x_1^n    | |a_1|   |  y_1  |
    # |1  x_2     x_2^2     ... x_2^n    | |a_2| = |  y_2  |
    # | .. ..                            | |...|   |  ...  |
    # |1  x_(n-1) x_(n-1_^2 ... x(n-1)^n | |a_n|   |y_(n-1)|
    
    for i in range(length):
        coeff[:, i] = x**i
    
    # Invert the matrix
    inverse = np.linalg.pinv(coeff)
    
    # calculate the coefficients
    coefficients = np.dot(inverse, y)
    return coefficients


x = np.array([-3.,-2.,-1.,0.,1.,3])
y = np.array([-80.,-13.,6.,1.,5., 16])
coefficients = get_coefficients(x, y)
p = Polynomial(list(coefficients))
X = np.linspace(-3, 3, 50, endpoint=True)
F = p(X)
plt.plot(X,F)
plt.plot(x,y, 'ro')
print(x,y)
print(coefficients)
print(p)
