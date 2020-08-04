def Insertionsort(A):
    for i in range(1, len(A)):
        tmp = A[i]
        k = i
        while k > 0 and tmp < A[k - 1]:
            A[k] = A[k - 1]
            k -= 1
        A[k] = tmp


A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
Insertionsort(A)
print(A)