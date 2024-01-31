import numpy as np

def f(x):
    return np.sin(x) - np.sin(np.sin(x))

while True:
    a = float(input("Enter upper bound: "))
    b = float(input("Enter lower bound: "))

    if f(a) * f(b) <= 0:
        break
    else:
        print("Re-enter values")

tol = 1e-3
c = (a + b) / 2

while abs(f(c)) > tol:
    if f(a) * f(c) < 0:
        b = c
    elif f(c) * f(b) < 0:
        a = c
    c = (a + b) / 2

print("The root is approximately:", c)
print(np.abs(f(c)))
