A = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]
B =-42

def solve(A, B):
    A = sorted(A)
    
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if abs(A[i]-A[j])==abs(B):
                return 1
            if A[i]-A[j]>B:

                break    
    return 0        
            

print(solve(A,B))                