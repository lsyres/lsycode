# print("this is a sycn test to github")
# print("again")
# print("again and again")
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
# x = symbols('x')

f = lambda x : (x-3)*(x-2)*(x-1)*x*(x+1)*(x+2)*(x+3)

# d = diff(f(x),x)

x = np.linspace(-3.1,3.1,1000)
y = [f(i) for i in x]


# plt.figure(figsize=(9,6))
# plt.plot(x,y)
# plt.show()

lr = 0.001
s = np.random.choice(x, 1)
xx = s
best = f(xx)
bestlist = []
delta = lambda x : 7*x**6 - 70*x**4 + 147*x**2 - 36
for i in range(50):
    xx = xx - lr*delta(xx)
    if best > f(xx):
        best = f(xx)
        # bestlist.append(best)
        print(best)


# plt.figure(figsize=(9,6))
# plt.plot(bestlist)
# plt.show()