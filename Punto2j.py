import math 

def f(x):
	return (x*(math.e**x))
def formula(y,a,b):
	f= (b-a)/2.0
	f=f* y
	f=f+((b+a)/2.0)
	return f

def gauss(a,b):
	raiz=math.sqrt(1.0/(3.0))
	raiz2=math.sqrt(3.0/(5.0))
	g= (b-a)/2.0
	f1=formula(raiz,a,b)
	f2=formula(raiz*-1,a,b)
	g=g*(f(f1)+f(f2))
	return g

valor= gauss(1.0,1.25)+gauss(1.25,1.5)+gauss(1.5,1.75)+gauss(1.75,2.0)
v1=1.0
v2=1.000001
s= 0.000001
acum=0.0
cont=0
while (v2<=2.0):
	acum=acum+gauss(v1,v2)
	v1=v1+s
	v2=v2+s
	cont=cont+1

print ("%.10f"%gauss(1.0,2.0),"%.10f"%valor,"%.10f"%acum,"Particiones",cont)
	

