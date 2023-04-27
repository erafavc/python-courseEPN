# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:52:18 2023

@author: Administrador
"""

"""
PARA LISTAR 
!conda list

PARA INSTALAR MODULOS
pip install numpy
!conda install numpy    <--no funciona bien"""

from math import sin
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.optimize import fsolve


"""NUMPY"""
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

"""MATPLOTLIB"""
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

"""SYMPY"""
x = sp.symbols('x')
expr = (x-4)
sol = sp.solve(expr)
print(sol)
"""expr = x - 4*sin(x) NO FUNC CON sin DE MATH NI np.sin"""
x = sp.Symbol('x')
expr = x - 4*sp.sin(x)
print(sp.nsolve(expr,x,2))

x1 = sp.Symbol('x1')
y1 = sp.Symbol('x2')
f1 = 3 * x1**2 - 2 * y1**2 - 1
f2 = x1**2 - 2 * x1 + y1**2 + 2 * y1 - 8
print(sp.nsolve((f1, f2), (x1, y1), (-1, 1)))



