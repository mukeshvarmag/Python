A = [3,5,6]
A = list(filter(lambda x : x > 0, A))

A.sort()
B=[]
for i in range(len(A)):
    if(A[i]!=i+1):
        B.append(i+1)
print(B[0])
    

