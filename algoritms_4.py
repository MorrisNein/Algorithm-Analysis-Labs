# -*- coding: utf-8 -*-

import math
import random
import numpy as np
from scipy.optimize import minimize
from scipy import optimize
from matplotlib import pyplot as plt
import tqdm

"""#Functions"""

random.seed(42)

def f_rational(x, a, b, c, d):
    return (a * x + b) / (x ** 2 + c * x + d)

def f_x(x):
  return 1 / (x ** 2 - 3 * x + 2)

def gen_y(x):
  if f_x(x) < -100:
    y_k = -100 + np.random.normal(0, 1)
  elif f_x(x) >= -100 and f_x(x) <= 100:
    y_k = f_x(x) + np.random.normal(0, 1)
  elif f_x(x) > 100:
    y_k = 100 + np.random.normal(0, 1)
  return y_k

def least_squares(ab):
    a, b, c, d = ab
    global x, y
    global func
    return np.sum( (func(x, a, b, c, d) - y)**2) / x.shape[0]

def least_squares_lm(ab):
    a, b, c, d = ab
    global x, y
    global func
    return ((func(x, a, b, c, d) - y) / x.shape[0])

"""#Data generation"""

random.seed(42)


max_x = 1000

x = np.array([3 * k / 1000 for k in np.arange(0, max_x + 1, 1)])
y = np.array([gen_y(x[k]) for k in range(len(x))])

y_real = np.array([f_x(x[k]) for k in range(len(x))])

"""#Levenberg-Marquardt algorithm"""

ab_init = [1, 1, 1, 1]
func = f_rational
opt_rat_1 = optimize.least_squares(fun=least_squares_lm, x0=ab_init, method='lm', verbose=1)

"""#Nelder-Mead algorithm"""

ab_init = [1, 1, 1, 1]
func = f_rational
opt_rat_2 = optimize.minimize(least_squares, ab_init, method='nelder-mead', options={'xatol': 1e-3, 'disp': True})

"""#Annealing"""

ab_init = [1, 1, 1, 1]
func = f_rational
opt_rat_3 = optimize.dual_annealing(least_squares, bounds=list(zip([-5]*4, [5]*4)))
opt_rat_3

"""#Differential evolution"""

ab_init = [1, 1, 1, 1]
func = f_rational
opt_rat_4 = optimize.differential_evolution(least_squares, bounds=list(zip([-5]*4, [5]*4)))
opt_rat_4

"""#Plot"""

plt.figure(figsize=(18,9))
fig1 = plt.scatter(x, y, c='grey')
#fig2 = plt.plot(x, y_real, c='red')
fig3 = plt.plot(x, f_rational(x, opt_rat_1.x[0], opt_rat_1.x[1], opt_rat_1.x[2], opt_rat_1.x[3]), label='LM')
fig4 = plt.plot(x, f_rational(x, opt_rat_2.x[0], opt_rat_2.x[1], opt_rat_2.x[2], opt_rat_2.x[3]), label='Nelder-Mead')
fig5 = plt.plot(x, f_rational(x, opt_rat_3.x[0], opt_rat_3.x[1], opt_rat_3.x[2], opt_rat_3.x[3]), label='Annealing')
fig6 = plt.plot(x, f_rational(x, opt_rat_4.x[0], opt_rat_4.x[1], opt_rat_4.x[2], opt_rat_4.x[3]), label='Differential evolution')
plt.legend()
plt.grid(True)
plt.show()