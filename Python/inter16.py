A=[(1,3),
    (2,6),
    (8,10),
    (15,18)]

B=[]
for i in range(len(A)-1):
    if (A[i][1]>A[i+1][0]):
        B.append((A[i][0],A[i+1][1]))
    else:
        B.append((A[i+1][0],A[i+1][1]))

print(B)