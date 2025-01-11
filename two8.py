A = [-4,3]
B = [-2, -2]
def merge(A, B):
    i=0
    j=0
    while j<len(B) and i<len(A):
        if A[i]<=B[j]:
            i = i + 1
        else:
            A.insert(i,B[j])
            i = i + 1
            j = j +1
    A.extend(B[j:])
    return A
print(merge(A,B))    