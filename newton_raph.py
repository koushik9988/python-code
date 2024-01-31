import numpy as np

def f(x):
    return x**2 - 4 + np.sin(x)*x
# derivative of function
def der_f(x):
    return 2*x + x*np.cos(x) + np.sin(x)

tol = 1e-4

x = float(input("enter initial guess:"))

while(np.abs(f(x)) > tol):
    x = x -(f(x)/der_f(x))

print("approximate root is:",x)
print(f(x))

