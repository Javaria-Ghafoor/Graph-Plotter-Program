import numpy as num
import matplotlib.pyplot as mplot

def Lagrange(points, x):
    sum = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]

        def L(i):
            value = 1
            for j in range(n):
                if i == j:   #to avoid undetermined L-value
                    continue
                xj, yj = points[j]
                value *= float(x - xj) / float(xi - xj)  #L-value
            return value

        sum += yi * L(i)
    return sum

myData = []
print "Welcome to the Graph Plotter Program. This program uses the"
print "Lagrange multipliers to formulate an interpolation for the "
print "missing data in your data set. The graph is thus plotted as "
print "a smooth curve."
R = input("Enter the maximum value of x in your data: ")
R += 1
M = input("Now, enter the minimum value of x in your data: ")
print "Enter x:-999 and y:-999 to terminate the data entering mode."
for i in range(M, R):
    x = input("x:")
    y = input("y:")
    if x == y == -999:
        break
    myData.append([x, y])
myData = num.array(myData)

interpolatedData = []
for i in range(R):
    interpolatedData.append([i, Lagrange(myData, i)])
interpolatedData = num.array(interpolatedData)
print "The interpolated value of y against each value of x is: "
print(interpolatedData)

mplot.plot(interpolatedData[:, 0], interpolatedData[:, 1], 'r')
mplot.show()
