import numpy as np
# Define matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# Matrix multiplication
C = np.dot(A, B)
print("Matrix Multiplication:")
print(C)
# Matrix inversion
D = np.linalg.inv(A)
print("\nMatrix Inversion:")
print(D)
# Eigen decomposition
E, F = np.linalg.eig(A)
print("\nEigen Decomposition:")
print("Eigenvalues:\n", E)
print("Eigenvectors:\n", F)
# Singular Value Decomposition (SVD)
G, H, I = np.linalg.svd(A)
print("\nSingular Value Decomposition:")
print("Left Singular Vectors:\n", G)
print("Singular Values:\n", H)
print("Right Singular Vectors:\n", I)
# Matrix trace
J = np.trace(A)
print("\nMatrix Trace:")
print(J)