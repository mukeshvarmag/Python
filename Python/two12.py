A=[4,1,1,2,3]
B=1


def removeElement(A, B):
    i=0
    j=0
    
    
    
    while i< len(A):
        
        if A[i]!=B:
            

            A[j]=A[i]
            
            j+=1
            
        
        i+=1
    return A[:j]
print(removeElement(A,B))            
                
