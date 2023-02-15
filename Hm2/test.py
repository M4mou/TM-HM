from math import *
from sympy import *

omega = 1
phi = 52
a = 32
b = 4
c = 39
d = 19
e = 32
O1A = 12
O2D = 32
O3E = 18
AB = 46
AD = 29
GH = 14
DE = 53
GF = 25
FH = 14
O4G = 20

def xA(t):
    return O1A * cos(omega * t + phi)
def yA(t):
    return O1A * sin(omega * t + phi)
def xB(t):
    xa = xA(t)
    ya = yA(t)
    x, y= symbols("x, y",real=True)
    system  = [(x-xa)**2 + (y - ya)**2 - AB**2 , x]
    solution = nonlinsolve(system,[x, y])
    return max(solution.args[1][1].evalf(),solution.args[0][1].evalf())
    
print(xB(0))