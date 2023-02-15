A = [10, 5, 1, 0, 2]
(B, C) = (6, 8)


def count(A,B,C):
    
    cnt=0
    for i in range(len(A)):
        sum=0
    
        
        j=i
        while sum <=C and j< len(A):
            sum = sum+A[j]

            if sum <=C and sum >=B:
                cnt+=1            

            

   
            j+=1    


            
    return cnt
print(count(A,B,C))    