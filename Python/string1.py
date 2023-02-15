A = A = ["abab"]


def longestCommonPrefix(A):

    sum=""
    min_len=[]
    if len(A)==1:
        return A[0]

    for i in range(0,len(A)):
        min_len.append(len(A[i]))
    n=min(min_len)

    for i in range(0,n):
        for j in range(1,len(A)):
            if (A[j][i]==A[j-1][i]):
                false=1
            else:
                false=0    
        if(false==1):
            sum=sum+A[j][i]
    return sum 
   
print(longestCommonPrefix(A))        