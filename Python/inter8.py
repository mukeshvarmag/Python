def solve(A):
    a = [[] for i in range(A)]
    
    for i in range(A):
        for j in range(i+1):
            if ( j<i ):
                if (j == 0):
                    a[i].append(1)
                else:
                    print(a[i-1][j] + a[i-1][j-1])
                    a[i].append(a[i-1][j] + a[i-1][j-1]) 
            elif ( j == i):
                a[i].append(1)


                
    return a

print(solve(5))
