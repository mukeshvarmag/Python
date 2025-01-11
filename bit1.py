A=2

def numSetBits(A):
    x=[]
    j=32
    count=0
    while j>=0:
        x.append(A%2)
        A=A//2
        j=j-1
    for i in x:
        if i ==1:
            count=count+1
          
    return count,    x[::-1]        
print(numSetBits(A))