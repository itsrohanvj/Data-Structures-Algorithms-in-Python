def BubbleSort(A):
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if A[k] < A[k - 1]:
                swap(A, k, k - 1)

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
BubbleSort(A)
print(A)
