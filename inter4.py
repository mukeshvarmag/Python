A = [9, 9, 9, 9]

n = len(A)


for i in range(n-1,-1,-1):
    if (A[i] !=9):
        A[i]=A[i]+1
        while (A[0]==0):
            del A[0]
        break
    else:
        A[i]=0
else:
    A.insert(0,1)

print(A)