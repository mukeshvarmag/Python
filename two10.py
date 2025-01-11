A = [1,1,2,3,4,4]

def removeDuplicates(A):
    i=0
    j=i+1
    length=len(A)
    while(j<len(A)):
        if(A[i]==A[j]):
            j+=1
        else:
            i+=1
            A[i]=A[j]
    A=A[:i+1]
    if(i<length):
        A[i]='\0'

    return A
    

print(removeDuplicates(A))