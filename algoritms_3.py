# -*- coding: utf-8 -*-

import math
import random
import numpy as np
from scipy.optimize import minimize
from scipy import optimize
from matplotlib import pyplot as plt
import tqdm

"""# Functions"""

def f_linear(x, a, b):
    return a * x + b

def f_rational(x, a, b):
    return a / ( 1 + b * x )

def least_squares(ab):
    a, b = ab
    global x, y
    global func
    return np.sum( (func(x, a, b) - y)**2) / x.shape[0]

def least_squares_lm(ab):
    a, b = ab
    global x, y
    global func
    return ((func(x, a, b) - y) / x.shape[0])
  
def gradient_descent_lin(fun, x0, lr, n_iter, eps):
  m, c = x0
  n = float(len(x)) # Number of elements in X

# Performing Gradient Descent 
  for i in range(n_iter): 
      Y_pred = m*x + c  # The current predicted value of Y
      D_m = (-2/n) * sum(x * (y - Y_pred))  # Derivative wrt m
      D_c = (-2/n) * sum(m * y - Y_pred)  # Derivative wrt c
      m = m - lr * D_m  # Update m
      c = c - lr * D_c  # Update c
      if abs(lr * D_m) < eps and abs(lr * D_c) < eps:
        print('N iter = ', i)
        break
  print('N iter = ', i)
  return (m, c)    

def gradient_descent_rat(fun, x0, lr, n_iter, eps):
  m, c = x0
  n = float(len(x)) # Number of elements in X

# Performing Gradient Descent 
  for i in range(n_iter): 
      Y_pred = m*x + c  # The current predicted value of Y
      D_m = (2/n) * sum(y/(1+b*x) - (a/(1+b*x)**2))  # Derivative wrt m
      D_c =  2/n * sum((2 * b * a * (y - a /(1+b*x))) / (1 + b * x)**2)  # Derivative wrt c
      m = m - lr * D_m  # Update m
      c = c - lr * D_c  # Update c
      if abs(lr * D_m) < eps and abs(lr * D_c) < eps:
        print('N iter = ', i)
        break
  print('N iter = ', i)
  return (m, c)

random.seed(42)
a, b = random.random(), random.random()

max_x = 100

x = np.array([k / 100 for k in np.arange(0, max_x + 1, 1)])
y = np.array([a * x[k] + b + np.random.normal(0, 1) for k in range(len(x))])
y_real = np.array([a * x[k] + b for k in range(len(x))])

"""#Linear

##Gradient descent
"""

ab_init = [1, 1]
func = f_linear
opt_lin_1 = gradient_descent_lin(func(x, a, b), ab_init, 0.001, 10**5, 0.001)

"""##Conjunctive gradients"""

ab_init = [1, 1]
func = f_linear
opt_lin_2 = minimize(least_squares, ab_init, method='CG', options={'xatol': 1e-3, 'disp': True})

"""##Newton's method"""

ab_init = [1, 1]
func = f_linear
opt_lin_3 = minimize(least_squares, ab_init, method='BFGS', options={'xatol': 1e-3, 'disp': True})

"""##Levenberg-Marquardt algorithm"""

ab_init = [1, 1]
func = f_linear
opt_lin_4 = optimize.least_squares(fun=least_squares_lm, x0=ab_init, method='lm', verbose=1)

"""##Plot"""

plt.figure(figsize=(18,9))
fig1 = plt.scatter(x, y, c='grey')
fig2 = plt.plot(x, y_real, label='real')
fig3 = plt.plot(x, f_linear(x, opt_lin_1[0], opt_lin_1[1]), label='gradient descent')
fig4 = plt.plot(x, f_linear(x, opt_lin_2.x[0], opt_lin_2.x[1]), label='conjunctive gradients')
fig5 = plt.plot(x, f_linear(x, opt_lin_3.x[0], opt_lin_3.x[1]), label='newton')
fig6 = plt.plot(x, f_linear(x, opt_lin_4.x[0], opt_lin_4.x[1]), label='LM')
plt.legend()
plt.grid(True)
plt.show()

"""#Rational

##Gradient descent
"""

ab_init = [1, 1]
func = f_rational
opt_rat_1 = gradient_descent_rat(func(x, a, b), ab_init, 0.001, 10**5, 0.0001)

"""##Conjunctive gradients"""

ab_init = [1, 1]
func = f_rational
opt_rat_2 = optimize.minimize(least_squares, ab_init, method='CG', options={'xatol': 1e-3, 'disp': True})

"""##Newton's method"""

ab_init = [1, 1]
func = f_rational
opt_rat_3 = optimize.minimize(least_squares, ab_init, method='BFGS', options={'xatol': 1e-3, 'disp': True})

"""##Levenberg-Marquardt algorithm"""

ab_init = [1, 1]
func = f_rational
opt_lin_4 = optimize.least_squares(fun=least_squares_lm, x0=ab_init, method='lm', verbose=1)

"""##Plot"""

plt.figure(figsize=(18,9))
fig1 = plt.scatter(x, y, c='grey')
fig2 = plt.plot(x, y_real, label='real')
fig3 = plt.plot(x, f_rational(x, opt_rat_1[0], opt_rat_1[1]), label='gradient_descent')
fig4 = plt.plot(x, f_rational(x, opt_rat_2.x[0], opt_rat_2.x[1]), label='conjunctive gradients')
fig5 = plt.plot(x, f_rational(x, opt_rat_3.x[0], opt_rat_3.x[1]), label='newton')
fig6 = plt.plot(x, f_rational(x, opt_lin_4.x[0], opt_lin_4.x[1]), label='LM')
plt.legend()
plt.grid(True)
plt.show()