A = [100,100,100,100]
def maxIndexDiff(A):
    n=len(A)
    maxDiff = 0
    for i in range(0, int(n/2-1)):
        j = n - i
        if j>=i:
            if A[j] >= A[i] and maxDiff <= (j - i):
                maxDiff = j - i
            
 
    return maxDiff

print(maxIndexDiff(A))      