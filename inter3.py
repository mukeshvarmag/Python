"""
A = []

A = [int(item) for item in input().split()]

n = len(A)

B = int(input())
"""
A = [ 0, 0, 1, 1, 1, 0, 0, 1]
B = 3


def solve(A, B):
    i= 0
    
    res=0
    while(i<len(A)):
        j = min(i+B-1,len(A)-1)
        flag = False
        while(flag==False and j>0 and j > i-B+1):
            if (A[j]==1):
                flag = True
                res +=1
            j-=1
        i = j+1+B    
        if(flag==False):
            return -1
    return res    

print(solve(A,B))        




