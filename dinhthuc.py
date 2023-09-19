import numpy as np

n = int(input("Nhap n:"))

A = np.zeros((n,n), dtype = int)

for i in range (0,n):
    for j in range (0,n):
        x = int(input(f"A[{i+1}],[{j+1}] = "))
        A[i][j] = x

print(np.linalg.inv(A))