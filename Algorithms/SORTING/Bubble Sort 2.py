# OPTIMISED BUBBLE SORT.

def BubbleSort(A):
    swapped = 1
    for i in range(len(A)):
        if (swapped == 0):
            return

        for k in range(len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                swap(A, k, k - 1)
                swapped = 1


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
BubbleSort(A)
print(A)
