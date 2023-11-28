import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (x - 1)

H = []
integral_values = []  

n_val = np.arange(1, 10001)  

a =  -2
b =   3

for n in n_val:
    h = (b - a) / n
    H.append(h)
    k = 0.5 * h * (f(a) + f(b))
    
    for n0 in range(1, n):
        if (a + n * h != 1):
            k += h * f(a + n * h)

    integral_values.append(k)

#exact_value = np.exp(b) - np.exp(a)
exact_value = np.log(2/3)
print(exact_value)

#error = abs(exact_value - integral_values)
error = [abs(exact_value - value) for value in integral_values]

plt.plot(H,error )
plt.xlabel('Step Size (h)')
plt.ylabel('error')
#plt.yscale('log')  
#plt.xscale('log')
plt.show()
