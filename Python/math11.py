A=[1,0,1]
def arrange(A):
    n = len(A)
    for i in range(n):
        
        A[i] += (A[A[i]]%n)*n
        
    for i in range(n):
        
        A[i] = A[i]//n
    return A
print(arrange(A))
