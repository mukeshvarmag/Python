A="abcdfe"
B="cd"
def place(A,B):

    size = len(B)
    for i in range(len(A)):
            # substring comparison
        if A[i:i+size]==B:
            return i
        # return -1
        # no match found
    return -1
            
            
print(place(A,B))




            