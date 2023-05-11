import numpy as np

def load_linar_example1():
    X = np.array([[1,4],[1,8],[1,13],[1,17]])
    Y = np.array([7,10,11,14])
    return X,Y

X,Y = load_linar_example1()
print(X)
print(Y)
