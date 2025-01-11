A = [1 , 2 , 2 ,1 ]
def repeatedNumber(A):
    n=len(A)
    seen=[False]*n
    
    for x in A:
        

        if seen[x]==True:
            return x
        else:
            seen[x]=True
    return -1
print(repeatedNumber(A))            