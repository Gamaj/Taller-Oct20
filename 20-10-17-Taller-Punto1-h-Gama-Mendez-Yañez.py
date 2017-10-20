import math
import numpy as np

def f(x):
		return (math.log(x))
		
def segundaDerivadaf(x):
		return (-1/(x**2))

def aproxfsegunda(x,h):
		a=f(x+2*h)-2*f(x+h)+f(x)
		a=a/(h**2)
		return a
print ("h=0.01",aproxfsegunda(1.8,0.01))
print ("h=0.001",aproxfsegunda(1.8,0.001))
print ("h=0.0001",aproxfsegunda(1.8,0.0001))
print ("h=0.00001",aproxfsegunda(1.8,0.00001))
#print ("Segunda Derivada",segundaDerivadaf(1.8))
