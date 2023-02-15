A=55
def convertToTitle(A):
    s=""
    while A>0:
        if A%26==0:
            c=chr(26+64)
        else:
            c=chr(int(A%26)+64)
        s=c+s
        
        A=(A-1)//26
        
    return s
print(convertToTitle(A))    
print("1"+"2")
