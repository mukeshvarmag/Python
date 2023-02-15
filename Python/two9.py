A = [1,2,3,4,5]

B=[2,3,3,5]

def inter(A,B):
    i=0
    j=0
    x=[]
    while i<len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j+= 1
        else:
            x.append(B[j])
            j += 1
            i += 1
    return x        



print(inter(A,B))    
