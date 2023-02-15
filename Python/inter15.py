A = [1,3,2,5,4,6]

def printUnsorted(A):
    B=sorted(A)
    if (B==A):
        return -1
    else:
        L = [ i for i in range(len(A)) if A[i]!=B[i] ]
        return [min(L),max(L)]

print(printUnsorted(A))


