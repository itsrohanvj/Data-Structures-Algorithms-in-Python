def prefixTable(pattern):
    m = len(pattern)
    F = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = F[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        F[q] = k
    return F

def KMP(text, pattern):
    n = len(text)
    m = len(pattern)
    F = prefixTable(pattern)
    q = 0
    for i in range(n):
        if pattern[q] == text[i]:
            q = q + 1
            i = i+1
        if q == m:
            q = F[q - 1]
            print(i - m + 1)
        elif i < n and pattern[q] != text[i]:
            # Do not match lps[0..lps[q-1]] characters,
            # they will match anyway
            if q != 0:
                q = F[q - 1]
            else:
                i += 1
    return

#calling function
print (KMP("ROHAN VIJAY ROHAN", "ROHAN"))

