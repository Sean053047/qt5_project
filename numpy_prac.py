import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
print(type(x))
print(x.shape)
print(x.dtype)
print(x[0,0])
y = x[:,1]
print(y)
y[0]=11
print(y)
print(x)
# a = np.arange(15).reshape(3,5)
# print(a.dtype.name)