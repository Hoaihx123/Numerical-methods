from numpy import linalg
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [5, 6, 8, 10, 12, 13, 12, 10, 8, 10, 8, 11, 7, 9, 11, 10, 9, 12, 11, 6]

# Функция для вычисления коэффициентов аппроксимирующей кривой с полиномы по m-й порядок
def coefficients(m):
    C = []
    b = []
    for i in range(m + 1):
        Ci = []
        bi = 0
        for j in range(m + 1):
            cij = 0
            for xi in x:
                cij += xi ** (i + j)
            Ci.append(cij)
        for k in range(len(x)):
            bi += (x[k] ** i) * y[k]
        C.append(Ci)
        b.append(bi)
    a = linalg.solve(C, b)
    return a

# Функия для вычисления значении многочлены с коэффициетами a в точке x
def f(x, a):
    resul = 0
    for k in range(len(a)):
        resul += a[k] * x ** k
    return resul

# Вычисление отклонений
a = coefficients(5)
lf = []
s = 0
for i in range(len(x)):
    fi = f(x[i], a)
    s += (fi-y[i])**2
    lf.append(fi)

func = ""
for i in range(len(a)):
    ar = round(a[i], 5)
    if ar > 0:
        if i == 0:
            func += str(ar)
        elif i == 1:
            func += "+"+str(ar)+"x"
        else:
            func += "+"+str(ar)+"x^"+str(i)
    elif ar < 0:
        if i == 0:
            func += str(ar)
        elif i == 1:
            func += str(ar)+"x"
        else:
            func += str(ar)+"x^"+str(i)
print("Аппроксимирующая кривая: f(x) =", func)
print("Сумма квадратов отклонений: ", s)

# plt.plot(x, y)
plt.plot(x, lf)
plt.title("f(x)="+func)
plt.xlabel("x")
plt.ylabel("f(x)")
for i in range(len(x)):
    plt.plot(x[i], y[i], 'ro')
plt.show()