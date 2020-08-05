#METHOD 1: NORMAL WAY
def BinarySearchIterative(numbersList, value):
    low = 0
    high = len(numbersList) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbersList[mid] > value:
            high = mid - 1
        elif numbersList[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(BinarySearchIterative(A, 277))

#METHOD 2: RECURSIVE STYLE
def BinarySearchRecursive(numbersList, value, low=0, high=-1):
    if not numbersList: return -1
    if (high == -1): high = len(numbersList) - 1
    if low == high:
        if numbersList[low] == value:
            return low
        else:
            return -1
    mid = low + (high - low) // 2
    if numbersList[mid] > value:
        return BinarySearchRecursive(numbersList, value, low, mid - 1)
    elif numbersList[mid] < value:
        return BinarySearchRecursive(numbersList, value, mid + 1, high)
    else:
        return mid


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(BinarySearchRecursive(A, 321))