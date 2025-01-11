A=[20, 15, 10, 17]

B=7

def possible(A,B,mid):
    wood = 0
    for i in range(len(A)):
        if A[i]>mid:

            wood = wood +A[i]-mid
    if(wood>=B):
        return True 
    else:
        return False
def solve(A,B):
    start =0
    end = max(A)
    ans=-1
    while start<=end:
        mid = start+(end-start)//2

        if (possible(A,B,mid)):
            ans = mid
            start=mid +1
        else:
            end = mid -1
    return ans        

#Hi
print(solve(A,B))

