A = [0, 1, 2, 0, 1, 2]

def sor(A):
    lo = 0
    arr_size=len(A)
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if A[mid] == 0:
            A[lo], A[mid] = A[mid], A[lo]
            lo = lo + 1
            mid = mid + 1
        elif A[mid] == 1:
            mid = mid + 1
        else:
            A[mid], A[hi] = A[hi], A[mid]
            hi = hi - 1
    return A

print(sor(A))