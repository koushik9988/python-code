import numpy as np

def f(x):
    return 1 / (x - 1)

a = float(input("enter the lower limit of integration :"))
b = float(input("enter the upper limit of integration :"))
div = int(input("enter the no of division :"))

h = (b - a) / div
k = 0.5 * h * (f(a) + f(b))

for n in range(1, div):
    if (a + n * h != 1):
        k += h * f(a + n * h)

print("Numerically calculated value of the integral is:", k)

exact_value = np.log( abs(b-1) / abs(a-1))
print("Exact value of the integral is:", exact_value)

error = abs(exact_value - k)
print("Difference between exact value and numerical value:", error)
