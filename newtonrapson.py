import matplotlib.pyplot as plt
import numpy as np
import math
def f(x): return x * np.sin(x)+np.cos(x)
def g(x): return x * np.cos(x)


x=2.5
xi=x-(f(x)/g(x))
error= 0.00001
fig,ax=plt.subplots()
b=np.linspace(-7,7,200)
a=f(b)
ax.plot(b,a,label="f(x)=xsin(x)+cos(x)")

while(abs((xi-x)/xi)>error):
    x=xi
    xi=x-(f(x)/g(x))
print("Root: ",xi)



plt.xlabel("x")
plt.ylabel("f(x)")
ax.scatter(x,0,color='Red',marker='x',label=f'Real Root : {x}')
plt.legend()
ax.grid()
ax.set_title("Newton Raphson")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.show()
