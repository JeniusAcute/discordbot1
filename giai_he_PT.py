#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
n = int(input("Nhap n:"))

A = np.zeros((n,n), dtype = int)
B = np.zeros((n,n), dtype = int)

for i in range (0,n):
    for j in range (0,n):
        x = int(input(f"A[{i+1}],[{j+1}] = "))
        A[i][j] = x

for i in range (0,n):
    for j in range (0,1):
        x = int(input(f"B[{i+1}],[{j+1}] = "))
        B[i][j] = x

#A = np.array([(1,2),(3,4)])
#B = np.array([5,6])
try:
    A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
    print("A= ")
    print(A)
    print("B= ")
    print(B)
    print("Nghich dao= ")
    print(A1)
    X = np.dot(A1,B)
    print('Nghiem cua he:',X)

except:
    print("He phuong trinh vo so nghiem hoac vo nghiem")
    A2 = np.zeros((n,n+1), dtype = int)
    for i in range (0,n):
        for j in range (0,n):
            A2[i][j] = A[i][j]
    for i in range (0,n):
        A2[i][n] = B[i][0]
    rankA = np.linalg.matrix_rank(A)
    rankA2 = np.linalg.matrix_rank(A2)
    if rankA < rankA2:
        print("Vô nghiệm")
    elif (rankA == rankA2) and (rankA < n) and (rankA2 < n):
        print("Vô số nghiệm")
    #print(A2)
print(" ")