
n=int(input())

B = [int(item) for item in input().split()]


B.sort()

A=[]
for i in range(1,n+1):
    A.append(i)



  

   


miss=0
for i in range(0,len(A)):
    if i<n-1:
        if (A[i]-B[i]) !=0:
            miss=A[i]
            break

    if i==n-1:
        miss=A[i]        

print(miss)