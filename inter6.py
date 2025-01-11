A = [
    [1, 2, 3],
    [4, 5,6],
    [7, 8, 9] 
]

B=[
    [1, 2, 3],
    [4, 5,6],
    [7, 8, 9] 
]



n = len(A)
B = [[0 for i in range(n)] for j in range(n)]

print(B)
        
for i in range(n):
    for j in range(n):
        B[j][n-i-1] = A[i][j]
        

print(B)