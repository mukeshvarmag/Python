A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4


def search( A, B):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2
        print(mid)
        if B == A[mid]:
            return mid
        elif A[mid] <= A[high]:
            if( B > A[mid]) & (B <= A[high]):
                low = mid + 1
            else:
                high = mid - 1
        else:
            if (A[low] <= B) & (B < A[mid]):
                high = mid - 1
            else:
                low = mid + 1
    return -1

print(search(A,B))