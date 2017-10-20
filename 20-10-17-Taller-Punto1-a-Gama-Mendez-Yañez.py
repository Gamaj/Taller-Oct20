import math
import numpy as np

def f(x):
		return (math.log(x))
		
def segundaDerivadaf(x):
		return (-1/(x**2))

def f2(x,h):
		a=f(x+h)-f(x)
		a=a/h
		ans= segundaDerivadaf(x)
		m= (h/2)*ans
		m=abs(m)
		resultado = a-m
		return resultado
	 
		
print ("h",0.1,"Resultado",f2(1.8,0.1))
print ("h",0.01,"Resultado",f2(1.8,0.01))
print ("h",0.001,"Resultado",f2(1.8,0.001))
print ("h",0.0001,"Resultado",f2(1.8,0.0001))
print ("h",0.00001,"Resultado",f2(1.8,0.00001))		                   
