from math import *
import scipy.integrate

xe=lambda x:x*exp(x)
cuad=scipy.integrate.quad(xe,2,1)
print "Integrando con cuadratura de Gauss ",-1*cuad[0]," y el error es ",cuad[1]
