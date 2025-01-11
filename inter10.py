A = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ] ]

def diagonal(A):

    n =len(A)
    N = 2 * n - 1

    result = []
    B = []
     
    for i in range(N) :
       result.append([])
    
     

    for i in range(n) :
        for j in range(n) :
           result[i + j].append(A[i][j])

 

    return result          

print(diagonal(A))          

