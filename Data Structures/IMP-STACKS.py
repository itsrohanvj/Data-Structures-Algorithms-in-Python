
#STACKS
def removeAdjacentDuplicates(str):
    stkptr = -1
    i = 0
    size = len(str)
    while i < size:
        if (stkptr == -1 or str[stkptr] != str[i]):
            stkptr += 1
            str[stkptr] = str[i]
            i += 1
        else:
            while i < size and str[stkptr] == str[i]:
                i += 1
            stkptr -= 1
    stkptr += 1
    str = str[0:stkptr]
    print str
removeAdjacentDuplicates(['6', '2', '4', '1', '2', '1', '2', '2', '1'])

#-------------------------------------####################
#REVERSE STACK RECURRSIVELY
def reverseStack(stack):
    def reverseStackRecursive(stack, newStack=Stack()):
        if not stack.is_empty():
            newStack.push(stack.pop())
            reverseStackRecursive(stack, newStack)
        return newStack
    return reverseStackRecursive(stack)