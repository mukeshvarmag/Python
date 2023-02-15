import math
A=[1,5,4,3]

def maxArea(A):
    l = 0
    r = len(A) -1
    area = 0
        
    while l < r:
        area = max(area, min(A[l], A[r]) * (r - l))
        print(A[l],A[r],l,r)
        if A[l] < A[r]:
            l += 1
        else:
             r -= 1
        
    return area
print(maxArea(A))