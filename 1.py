
from math import fabs
def f(x):
    return 1.78*(x**5)+3.2*(x**4)-5*(x**3)-9.7*(x**2)+x-21
x0 = float(input("x0="))
e = float(input("e="))
print('-------------')
print('x=', x0, 'f(x)=', f(x0))
x1 = x0-f(x0)/100
print('x=', x1, 'f(x)=', f(x1))
while fabs(x1-x0) >= e:
    x0 = x1
    x1 = x0-f(x0)/100
    print('x=', x1, 'f(x)=', f(x1))





