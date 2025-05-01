import numpy as np
from scipy.integrate import quad
# These functions will calculate the nessesary integrals using scipy.integrate
def momentum(n,m,L):
    return quad(lambda x: ((m**2*np.pi**2)/(L**3)*(np.cos(((n-m)*np.pi*(x+L/2))/L) - np.cos(((n+m)*np.pi*(x+L/2))/L))),-L/2,L/2 )[0]
def potentialOne(n,m,L):
    return quad(lambda x: (1/L)*np.cos(x)*(np.cos(((n-m)*np.pi*(x+L/2))/L) - np.cos(((n+m)*np.pi*(x+L/2))/L)),-L/2,L/2)[0]
def potentialTwo(n,m,L):
    return quad(lambda x: (1/L)*x**2*(np.cos(((n-m)*np.pi*(x+L/2))/L) - np.cos(((n+m)*np.pi*(x+L/2))/L)),-L/2,L/2)[0]
# presision sets matrix size
precision = 50
# L sets length of infinite square well
L = 50
# create empty matrix filled with zeros
H = np.zeros((precision,precision))
Ec = .1
E0 = 1
l= -.95
# looping through the 2D array which represents the matrix
for n in np.arange(1,precision+1,1):
    for m in np.arange(1,precision+1,1):
        resultFromCos = potentialOne(n,m,L)
        resultFromSqaure = potentialTwo(n,m,L)
        # calculating the hamiltonian for a given row n and column m
        h = Ec * momentum(n,m,L) + (E0 * resultFromCos) + (E0 * (l+1) * .5 * resultFromSqaure)
        H[n-1,m-1] = h
E, v = np.linalg.eig(H)
#resurns indecies that would sort argument
sorted = np.argsort(E)
print("Gound state: " + str(E[sorted[0]]))
print("First excited state: "+ str(E[sorted[1]]))
print("Second excited state: "+ str(E[sorted[2]]))
print("Diff between First excited state and Gound state: " +str(E[sorted[1]]-E[sorted[0]]))
print("Diff between Second excited state and first state: " +str(E[sorted[2]]-E[sorted[1]]))

