import numpy as np
m,n=list(map(int,input().split()))
x=np.ones((n,m+1))
y=np.zeros((n,1))
for i in range(n):
    obs=np.array(list(map(float,input().split())))
    for j in range(m):
        x[i,j+1]=obs[j]
    y[i,0]=obs[m]
q=int(input())
xtest=np.ones((q,m+1))
for i in range(q):
    test=np.array(list(map(float,input().split())))
    for j in range(m):
        xtest[i,j+1]=test[j]

xtx=(x.T).dot(x)
xtxinv=np.linalg.inv(xtx)
xtxinvxt=xtxinv.dot(x.T)
b=xtxinvxt.dot(y)

for k in range(q):
    print(float(xtest[k].dot(b)))