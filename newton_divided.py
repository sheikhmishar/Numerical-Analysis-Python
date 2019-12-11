import numpy as np
import matplotlib.pyplot as plt

class Newtons_Divided_Differences:
    def __init__(self, differences, data_x):
        self.differences = differences
        self.data_x = data_x
        self.multiplierstring = ""
        # self.generalequation = "y = f(x) = " # TBI
        print(f"x = {data_x}\n")

    def __call__(self, x):
        """
        this function is for calculating y from given x using all the difference coefficients
        x can be a single value or a numpy
        the formula being used:
        f(x) = f [x0] + (x-x0) f[x0,x1] + (x-x0) (x-x1) f[x0,x1,x2] + . . . + (x-x0) (x-x1) . . . (x-xk-1) f[x0, x1, . . ., xk]

        work on this after implementing 'calc_div_diff'. Then you should have
        f[x0], f[x0,x1]. . . . . ., f[x0, x1, . . ., xk] stored in self.differences

        'res' variable must return all the results (corresponding y for x)
        """

        y = np.zeros(len(x)) #Initialization to avoid runtime error. You can change this line if you wish

        # place your code here!!!!!!!!!!!!!!!!!!!!!!!
        for i in range(len(y)):
            y[i] = self.newtonDiv(x[i])
        return y

    def newtonDiv(self, xi):
        res = 0
        addstr = f"y = f({xi}) = "
        for i in range(len(self.differences)):
            res += self.differences[i][0] * self.multiplier(xi, i)
            if i is not 0:
                addstr += " + "
            if self.differences[i][0] < 0:
                addstr += f'({self.differences[i][0]})'
            else:
                addstr += f'{self.differences[i][0]}'
            if self.multiplierstring is not "":
                addstr += f' * {self.multiplierstring}' #+ f' = {self.multiplier(xi, i)}'
        print(addstr + "\n")
        return res

    def multiplier(self, xi, i):
        res = 1
        mulstr = ""
        for j in range(i):
            res *= xi - self.data_x[j]
            if j is not 0:
                mulstr += " * "
            if(self.data_x[j] < 0):
                mulstr += f"({xi} - ({self.data_x[j]}))"
            else:
                mulstr += f"({xi} - {self.data_x[j]})"
        self.multiplierstring = mulstr
        return res

#basic rule for calculating the difference, implanted in the lambda function. You may use it if you wish
difference = lambda y2, y1, x2, x1: (y2-y1)/(x2-x1)


def calc_div_diff(x,y):
    assert(len(x)==len(y))
    #write this function to calculate all the divided differences in the list 'b'
    b = [[] for i in range(len(x))]

    #place your code here!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(len(x)):
        for j in range(len(x)-i):
            if(i==0):
                b[i].append(y[j])
            else:
                b[i].append(difference(b[i-1][j+1],b[i-1][j],x[j+i],x[j]))
    return b

def print_diff(diff):
    for i in range(len(diff)):
        if i is 0:
            print('y = ', end = '')
        print(diff[i])
    print()

data_x = np.array([-3.,-2.,-1.,0.,1.,3.,4.])
data_y = np.array([-60.,-80.,6.,1.,45.,30.,16.])
# data_x = np.array([10.,15.,20.,22.5])
# data_y = np.array([227.4,362.78,517.35,602.97])
differences = calc_div_diff(list(data_x), list(data_y))
obj = Newtons_Divided_Differences(list(differences), list(data_x))
print_diff(differences)

# #generating 50 points from -3 to 4 in order to create a smooth line
X = np.linspace(-3, 4, 50, endpoint=True)
# X = np.array([-2.999999, -2.01231, -0.93213, 0.6757757, 1.97578, 2.9466, 3.998654])
# X = np.array([10.,15.,20.,22.5])
# X = np.linspace(10.1, 22.49999, 4, endpoint=True)
F = obj(X)
plt.plot(X,F)
plt.plot(data_x, data_y, 'ro')
plt.show()