A=3
def numSetBits(A):
    x=[]
    j=32
    sum=0
    
    while j>0:
        x.append(A%2)
        A=A//2
        j=j-1
    y=x[::-1]
    for z in range(len(y)):
        
        sum=sum+y[z]*(2**z)
        
    return sum    


print(numSetBits(A))