import numpy
def f1(x,y,z):
    return x*z*z+x*x*y-3.75
def f2(x,y,z):
    return -1.5*x*y*z+2*(y**3)+3.7*x*x-10.825
def f3(x,y,z):
    return x*(z**3)+7*z*z*(y**3)+16
def f1x(x,y,z):
    return z*z+2*x*y
def f1y(x,y,z):
    return x*x
def f1z(x,y,z):
    return 2*x*z
def f2x(x,y,z):
    return -1.5*y*z+7.4*x
def f2y(x,y,z):
    return -1.5*x*z+6*y*y
def f2z(x,y,z):
    return -1.5*x*y
def f3x(x,y,z):
    return z**3
def f3y(x,y,z):
    return 21*z*z*y*y
def f3z(x,y,z):
    return 14*z*(y**3)

print("Решить систему нелинейных уравнений методом Ньютона:")
print("xz^2+x^2*y-5=1.25\n-1.5xyz+2y^3+3.7x^2=10.825\nxz^3+7z^2*y^3=-16")
x = float(input("x0="))
y = float(input("y0="))
z = float(input("z0="))
e = float(input("e="))
A = numpy.matrix([[f1x(x, y, z), f1y(x, y, z), f1z(x, y, z)], [f2x(x, y, z), f2y(x, y, z), f2z(x, y, z)], [f3x(x, y, z), f3y(x, y, z), f3z(x, y, z)]])
B = numpy.array([-f1(x, y, z), -f2(x, y, z), -f3(x, y, z)])
delta = numpy.linalg.solve(A, B)
x = x + delta[0]
y = y + delta[1]
z = z + delta[2]
print(x, y, z, f1(x, y, z), f2(x, y, z), f3(x, y, z))

while (delta[0]*delta[0]+delta[1]*delta[1]+delta[2]*delta[2]>e*e):
    A = numpy.matrix([[f1x(x, y, z), f1y(x, y, z), f1z(x, y, z)], [f2x(x, y, z), f2y(x, y, z), f2z(x, y, z)],
                     [f3x(x, y, z), f3y(x, y, z), f3z(x, y, z)]])
    B = numpy.array([-f1(x, y, z), -f2(x, y, z), -f3(x, y, z)])
    delta = numpy.linalg.solve(A, B)
    x = x + delta[0]
    y = y + delta[1]
    z = z + delta[2]
    print(x, y, z, f1(x, y, z), f2(x, y, z), f3(x, y, z))
