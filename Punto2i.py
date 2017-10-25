from sympy import *
import math
x=Symbol('x')

a=integrate(1/(1+x**2)**3, (x, 1, oo))
print "El valor de la integral (1/(1+x**2)**3 es ",a.evalf()

b= integrate(sin(x)/x, (x, 0, 1))
print "El valor de la integral sin(x)/x es ",b.evalf()
