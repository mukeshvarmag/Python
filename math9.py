import math
A=str("cab")
def findRank(A):
    def fact(n):
        if(n==0):
            return 1
        else:
            return (n*fact(n-1))%mod
    mod=1000003
    s=A
    ans=0
    n=len(s)
    for i in range(n-1):
        c=0
        for j in range(i+1,n):
            if s[j] < s[i]:
                c+=1
        ans+=(c*fact(n-i-1))%mod
    return(ans+1)%mod

print(findRank(A))