import sys
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def a(x):
    return 2.

def b(x):
    return -3.

def c(x):
    return 1.

def f(x):
    return (x-0.)*(x-0.)

beta = 1.
gamma = 2.
uR = -1.
n = 10 
h = 1. / n 
bignumber = 1000

def e(k, x):
    if (k == 0) and (0 <= x) and (x <= h):
        return (h - x) / h
    elif (k == n) and ((n - 1) * h <= x) and (x <= 1):
        return (x / h) - n + 1
    elif (k == n) or (k == 0):
        return 0
    else:
        x_k = k * h
        if (x <= x_k) and (x_k - h <= x):
            return (x / h) - k + 1
        elif (x <= x_k + h) and (x_k <= x):
            return -(x / h) + k + 1
        else:
            return 0


def derivadaE(k, x):
    if (k == 0) and (0 <= x) and (x <= h):
        return -1. / h
    elif (k == n) and ((n - 1) * h <= x) and (x <= 1):
        return 1. / h
    elif (k == n) or (k == 0):
        return 0
    else: 
        x_k = k * h
        if (x <= x_k) and (x_k - h <= x):
            return 1. / h
        elif (x <= x_k + h) and (x_k <= x):
            return -1. / h
        else:
            return 0


def integral1(i, j):
    ancho = 1. / bignumber
    suma = 0.
    for q in range(bignumber):
        x = q * ancho
        altura = derivadaE(j, x) * a(x) * derivadaE(i, x)
        area = altura * ancho
        suma += area
    return suma


def integral2(i, j):
    ancho = 1. / bignumber
    suma = 0.
    for q in range(bignumber):
        x = q * ancho
        altura = e(j, x) * b(x) * derivadaE(i, x)
        area = altura * ancho
        suma += area
    return suma


def integral3(i, j):
    ancho = 1. / bignumber
    suma = 0.
    for q in range(bignumber):
        x = q * ancho
        altura = e(j, x) * c(x) * e(i, x)
        area = altura * ancho
        suma += area
    return suma


def integral4(i):
    ancho = 1. / bignumber
    suma = 0.
    for q in range(bignumber):
        x = q * ancho
        altura = f(x) * e(i, x)
        area = altura * ancho
        suma += area
    return suma


def Be(i, j):
    return -beta * e(j, 0) * e(i, 0) - integral1(i, j) + integral2(
        i, j) + integral3(i, j)


def le(i):
    return -gamma * e(i, 0) + integral4(i)

print("Matriz:")
matriz = np.zeros((n + 1, n + 1))
matriz[n, n] = 1
for i in range(n):
    matriz[i, i] = Be(i, i)
    if i > 0:
        matriz[i - 1, i] = Be(i, i - 1)
        matriz[i, i - 1] = Be(i - 1, i)
matriz[n - 1, n] = Be(n, n - 1)
print(matriz)

print("\n", "Vector:")
vector = np.zeros((n + 1, 1))
for i in range(n):
    vector[i] = le(i)
vector[n] = uR
print(vector)

print("\n", "resultado:")
res = la.solve(matriz, vector)
print(res)

puntos = np.linspace(0.0, 1.0, n + 1)
valores = np.zeros(n + 1)
for i in range(n + 1):
    valores[i] = res[i]
plt.plot(puntos, res)
plt.show()