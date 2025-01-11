A=112

def isPalindrome(A):
    B=[]
    if(A<0):
        return 0
    if (A==0):
        return 1    
    while A>0:
        if (A%10==0):
            B.append(0)
            A=A//10

        else:
            B.append(A%10)
            A=A//10
       
    C=[]
    for j in B[::-1]:
        C.append(j)
    
    
    
    for i in range(len(B)):
        if(B[i]!=C[i]):
            return 0
        break    
                        
    return 1        
                        
   

print(isPalindrome(A))    