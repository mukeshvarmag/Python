A = [-1, 2, 1, -4]
target = 1
def threeSumClosest(A, B):
    A.sort()
    closest = None
    for i in range(len(A) - 2):
        j= i + 1 
        k=len(A) - 1
        while k > j:
            threeSum = A[i] + A[j] + A[k]
            if threeSum == B:
                return threeSum
            if closest is None or abs(B - threeSum) < abs(B - closest):
                closest = threeSum
            if threeSum < B:
                j += 1
            else:
                k -= 1
    return closest
