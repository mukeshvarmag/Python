A="aaabaaa"
def longestPalindrome(A):
    n=int(len(A))
    print(n)
    si=0
    maxlen=-1
    for i in range(2*n-1):
        div2=int(i/2)
        if i%2==0:
            r=div2-1
            l=div2+1
        else:
            r=div2
            l=div2+1
        check=False
        print(r,l,"***")
        while r>=0 and l<=n-1 and A[r]==A[l]:
            print(r,l,A[r],A[l]),
            r-=1
            l+=1
            check=True
        if check:
            lens=(l-1)-(r+1)+1
        else:
            lens=1
            #print("lens:",lens)
        if lens>maxlen:
            maxlen=lens
            si=r+1
    return A[si:si+maxlen]
print(longestPalindrome(A))    