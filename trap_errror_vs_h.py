import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #return np.exp(x)
    return 2*x + 3*x**2 - 4*x**3
def f1(x):
    return x**2 + x**3 - x**4

H = []  #empty array to store step sizes 
integral_values = []  

n_val = np.arange(1, 2001)  

a =  -2
b =   3

for n in n_val:
    h = (b - a) / n
    H.append(h)
    k = 0.5 * h * (f(a) + f(b))
    for i in range(1, n):
        k += h * f(a + i * h)

    integral_values.append(k)

#exact_value = np.exp(b) - np.exp(a)
exact_value = f1(3) - f1(-2)
print(exact_value)


#error = abs(exact_value - integral_values)
error = [abs(exact_value - value) for value in integral_values]

#print(error)
#print(H)


plt.plot(H,error )
plt.xlabel('Step Size (h)')
plt.ylabel('error')
#plt.yscale('log')  
#plt.xscale('log')
plt.show()
