A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
B = 2
start = 0
end=len(A)
c=[]
d=[]
while start<=end:
    mid=start+(end-start)//2
    for i in  range(0,mid):
        if B>0:
            if A[i]==0:
                A[i]=1
                B=B-1

                c.append(A[i])
    for i in range(end-1,mid,-1):
        if B>0:
            if A[i]==0:
                A[i]=1
                B=B-1
                d.append(A[i])
    if len(c)>len(d):
        end=mid-1
    else:
        start=mid
print(c,d)                                
