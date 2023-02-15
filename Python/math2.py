A = 9
def ispower(A):
    if A==1:
        return A
        
    for i in range(2,A):
        j=2
        while i**j<A:
            j=j+1
                
        if i**j==A:
            return 1
    return 0

print(ispower(A))