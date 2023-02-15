A = [-2,-1,0,1,2]

def threeSumarr(A):
    A.sort()


    x=[]
    for i in range(len(A)-2):
        j= i + 1 
        print(j)
        k=len(A) - 1   
        while k > j:
            threeSum = A[i] + A[j] + A[k]
            if threeSum == 0:
                z=[A[i],A[j],A[k]]
                z.sort()
                if z not in x:
                    x.append(z)
                

                

            if threeSum < 0:
                j += 1
            else:
                k -= 1
    return sorted(x)

print(threeSumarr(A))    