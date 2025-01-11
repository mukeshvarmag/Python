A = [11,1,2,3 ,15]
B = 10
def solve(A, B):
    n = len(A)
    i = 0
    j = 0
    sumsofar = 0
    cnt = 0
    while i<n:
        sumsofar += A[i]
        print(sumsofar,"##")
        while sumsofar >= B:
            sumsofar-= A[j]
            print(sumsofar,"**")
            j+=1
        cnt+=(i-j+1)
        i+=1
    return cnt


print(solve(A,B))
