A=6
B=9



def di(A,B):
    if B>A:
        A, B = B, A
    while B!=0:
        temp = B
        B = A%B
        A = temp
        print(A,B)
    return A

print(di(A,B))    
        