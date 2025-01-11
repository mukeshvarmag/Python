A =[1, 4, 5]
B = [2, 3]

def findMedianSortedArrays(A, B):
    m = len(A)
    n = len(B)
    if (m>n):
        A,B,m,n=B,A,n,m
    imin, imax,hl=0,m,(m+n+1)/2
    while(imin<=imax):
        i = (imin+imax)/2
        j = hl-i
        if (i<m and B[j-1]>A[i]):
            imin = i+1
        elif (i>0 and A[i-1]>B[j]):
            imax = i-1
        else:
            if i==0:
                max_left = B[j-1]
            elif j==0:
                max_left = A[i-1]
            else:
                max_left = max(A[i-1],B[j-1])
                
            if (m+n)%2 == 1:
                return max_left
            else:
                if i==m:
                    min_right=B[j]
                elif j==n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])
                return (max_left+min_right)/2.0