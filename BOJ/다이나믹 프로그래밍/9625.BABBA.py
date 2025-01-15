k = int(input())
A = [0] * 46
B = [0] * 46
B[1] = 1
A[2] = 1
B[2] = 1
for i in range(3, k + 1):
    A[i] = A[i - 1] + A[i - 2]
    B[i] = B[i - 1] + B[i - 2]
print(A[k], B[k])