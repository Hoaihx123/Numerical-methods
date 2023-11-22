import numpy as np
import matplotlib.pyplot as plt

A = np.zeros((2, 77))
for i in range(77):
    A[0, i] = 1+0.25*i
A[1, 0] = 5
A[1, 4] = 6
A[1, 8] = 8
A[1, 12] = 10
A[1, 16] = 12
A[1, 20] = 13
A[1, 24] = 12
A[1, 28] = 10
A[1, 32] = 8
A[1, 36] = 10
A[1, 40] = 8
A[1, 44] = 11
A[1, 48] = 7
A[1, 52] = 9
A[1, 56] = 11
A[1, 60] = 10
A[1, 64] = 9
A[1, 68] = 12
A[1, 72] = 11
A[1, 76] = 6

def L(x, i, j):
    l = float(1)
    for k in range(j, j+8):
        if (k != i):
            l *= (x-A[0, 4*k])/(A[0, 4*i]-A[0, 4*k])
    return l
def f(x, j):
    f = 0
    for i in range(j, j+8):
        f += L(x, i, j)*A[1, 4*i]
    return f

for i in range(16):
    A[1, i] = f(A[0, i], 0)

for i in range(1, 12):
    A[1, (i+3)*4+1] = f(A[0, (i+3)*4+1], i)
    A[1, (i+3)*4+2] = f(A[0, (i+3)*4+2], i)
    A[1, (i+3)*4+3] = f(A[0, (i+3)*4+3], i)

for i in range(60, 76):
    A[1, i] = f(A[0, i], 12)

for i in range(0, 77):
    print('f(', A[0, i], ')=', A[1, i])

plt.plot(A[0], A[1])
for i in range(0, 20):
    plt.plot(A[0, i*4], A[1, i*4], 'ro')
plt.show()