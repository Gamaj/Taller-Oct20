import math
import numpy as np

def f(x):
		return (math.e**x)*math.sin(x)
		
def f2(x,h):
		a=f(x+h)-f(x)
		a=a/h
		b= (h/2)
		return b
		
def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by the
    composite Simpson's rule, using n subintervals (with n even)"""

    if n % 2:
        return ("error")

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3
g=lambda x:(math.e**x)*math.sin(x)
s=lambda x:4+math.cos(x+1)
v1=simpson(g, 0.0, 1.2615, 100000)
v2=simpson(s, 0.0, 1.2615, 100000)
v3=simpson(g, 1.2615, 2.9703, 100000)
v4=simpson(s, 1.2615, 2.9703, 100000)

v1=v2-v1
v4=v3-v4


print (v1+v4)                   
