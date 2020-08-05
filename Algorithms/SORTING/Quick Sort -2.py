#OPTIMISED IN A PYTHONIC WAY
def quickSort(A,low,high):
   if low >= high:
    return
   pivot = A[low]
   i = low+1
   j = high
   while i <= j:
       while i <= j and A[i] <= pivot:
           i = i + 1
       while A[j] >= pivot and j >= i:
           j = j -1
       if j < i:
           break
       A[i], A[j] = A[j], A[i]

   A[low], A[j] = A[j], A[low]
   partitionPoint = j

   quickSort(A,low,partitionPoint-1)
   quickSort(A,partitionPoint+1,high)

A = [5, 1, 32, 54, 12, 6, 32, 2, 5, 19, 99, 9]
quickSort(A,0,len(A)-1)
print(A)
