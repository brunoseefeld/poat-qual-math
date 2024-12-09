
#We numerically estimate the lyapunov exponent of the random 
# matrix product introduced by KIEFER, this is an example where
# the maximal lyapunov exponent is not continuous at all parameters.



import numpy as np


#Our matrices:

A1=np.array([[1/2,0]  , [0, 2]  ])

A2=np.array([[0, -1],   [1, 0]])

# The probability p of  chosing A2

p=0.1

#The number of iterates N
N=10000

A=np.array([[1,0],[0,1]])

for i in range(N):
    k=np.random.binomial(1,p)

    if k==0: #the case that the product receives the hyperbolic matrix
        A=np.matmul(A1,A)
    else: #receives rotation
        A=np.matmul(A2,A)

print(np.log(np.linalg.norm(A,2))/N)


#sometimes we get some inf values


    




