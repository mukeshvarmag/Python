A=[3 ,1, 2, 5, 3]
def repeatedNumber(A):
    n = len(A)
    
    x = sum(A) - sum(set(A))
    print(sum(A))
    k = sum(A) - int(n*(n+1)/2)
    
    return [x,x-k]
print(repeatedNumber(A))    