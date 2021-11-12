import numpy as np
np.set_printoptions(legacy='1.13')
a,b = map(int, input().split())
x = np.array([input().split() for _ in range(a)],int)
y = np.array([input().split() for _ in range(a)],int)
print(np.add(x, y)) 
print(np.subtract(x, y))
print(np.multiply(x, y))
print(np.array(x/y,int))
print(np.mod(x, y))
print(np.power(x, y))

