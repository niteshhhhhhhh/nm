import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [-9, 1, 35, 105, 223]
n = len(x)

diff = np.zeros((n, n))
diff[:, 0] = y 

for i in range(1, n):
    for j in range(n - i):
        diff[j][i] = diff[j+1][i-1] - diff[j][i-1]

for i in range(n):
    print(f'{x[i]:0.2f}', end='')
    for j in range(n - i):
        print(f'\t\t{diff[i][j]}', end='')
    print()

a = 3
h = x[1] - x[0] 
p = (a - x[0]) / h

interpolated_value = diff[0][0]
prod_p = 1
for i in range(1, n):
    prod_p *= (p - i + 1)
    interpolated_value += (prod_p * diff[0][i]) / np.math.factorial(i)

print(f"\nInterpolated value at x = {a} is {interpolated_value}")

