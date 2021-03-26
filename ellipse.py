import sympy as sy #symbolic computations
from math import sqrt
from numpy import pi
import matplotlib.pyplot as plt

x = sy.Symbol('x')


def circumference(a, b, t):
    result = 0
    stop = False
    x = 0
    y = b
    how = 0
    while(stop == False):
        x_next = next_point(x, y, a, b, t)
        y_next = sqrt(abs(((b**2) - ((b/a)**2)*(x_next**2))))
        how += 1
        x = x_next
        y = y_next
        if (abs(x_next - a) < a / 100):
            stop = True
        else:
            result += t
    return result*4
    
def next_point(x, y, a, b, t):
    stop = False
    x_next = x
    iterator_count = 0 
    iterator = t / 20
    while(stop == False):
        x_next += iterator
        y_next = sqrt(abs(((b**2) - ((b/a)**2)*(x_next**2))))
        length = sqrt(abs(((y_next-y)**2) + ((x_next-x)**2)))
        if (abs(length - t) < t / 4):
            stop = True
        if (length > t):
            iterator /= 2
        if (iterator_count > 100):
            stop = True
        iterator_count += 1
    return x_next

def approximation(a,b):
    return 2*(pi)*(((1/2)*((a**2)+(b**2))))**(1/2)

a = int(input("A: "))
b = int(input("B: "))

r = [0.001, 0.01, 0.2, 0.25, 0.3, 0.4, 0.5, 0.0005]
k = list()
m = list()
for i in r:
    k.append(circumference(a,b,i))
for j in range(len(k)):
    k[j] = abs(k[j]-approximation(a,b))
for j in range(len(k)):
    m.append(abs(k[j] / approximation(a,b)))
print("Approximation by formyla:" , approximation(a,b))
print("Errors with different t values:")

for i in range(len(k)):
    print("t: ",r[i], " Absolute Error: " ,k[i])
    
plt.figure(figsize=(5,5))
plt.scatter(r,k)
plt.xlabel("T")
plt.ylabel("Absolute Error")


plt.figure(figsize=(5,5))
plt.scatter(r,m)
plt.xlabel("T")
plt.ylabel("Relative Error")