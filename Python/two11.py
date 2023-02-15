A = [1,1,1,2,2,3,4]


def removeDuplicates(A):
    i = 2
    fp = 2
    while i < len(A):
        if A[fp-1] != A[i] or A[fp-2] != A[i]:
            A[fp] = A[i]
            fp += 1
        i += 1
    return fp
print(removeDuplicates(A))    