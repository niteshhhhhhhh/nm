import numpy as np

n=int(input("Enter no of unknowns:"))
a=np.zeros((n,n+1))
x=np.zeros(n)

print("Enter the augumented matrix coeffient:")
for i in range(n):
    for j in range(n+1):
        a[i][j]=float(input(f"a[{i}][{j}]:"))

print(a)

for i in range(n):
    if(a[i][j] == 0):
        print("Zero is detected")

    for j in range(n):
        if i!=j:
            ratio=a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio*a[i][k]


print(a)

for i in range(n):
    x[i]=a[i][n]/a[i][i]
 
print("Solution:")

for i in range(n):
    print('X%d = %0.2f' %(i,x[i]))
