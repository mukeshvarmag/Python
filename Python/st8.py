A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3

def maxA(A):
    ans=[]
    maxout=max(A[0:B])
    ans.append(maxout)

    for i in range(B,len(A)):
        if A[i] > maxout:
            ans.append(A[i])
            maxout=A[i]
        else:
            ans.append(maxout)
    return ans

print(maxA(A))             
