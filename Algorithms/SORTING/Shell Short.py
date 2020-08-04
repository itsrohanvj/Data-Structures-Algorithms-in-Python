def ShellSort(A):
    sublistcount = len(A) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(A, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", A)
        sublistcount = sublistcount // 2

def gapInsertionSort(A, start, gap):
    for i in range(start + gap, len(A), gap):
        currentvalue = A[i]
        position = i
        while position >= gap and A[position - gap] > currentvalue:
            A[position] = A[position - gap]
            position = position - gap

        A[position] = currentvalue

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
ShellSort(A)
print(A)

