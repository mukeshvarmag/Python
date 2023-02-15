B=7

def insert(A,B):

    start=0

    end=len(A)

    while start<end:

        mid=start+(end-start)//2

        print(A[mid])

        if(A[mid]<B):

            start=mid+1

        else:
            end=mid

    return start

print(insert([2,4,5,6,7,8,9],B))                