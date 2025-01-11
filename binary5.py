A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B=5

def books(A, B):
        
    def func(A , mid ):
        sum1 = 0
        count = 1
        for i in range(0,len(A)):
            sum1 = sum1 + A[i]
        
            if(sum1 > mid):
                sum1 = A[i]
                count = count + 1
        
        return count
        
    if(B > len(A)):
        return -1
    else:
        l = max(A)
        r = sum(A)
            
        while(l<=r):
            mid = l + int((r-l)/2)
            print(mid,"---mid")
            k = func(A , mid)
            if(k <= B):
                print(k,"---fun")
                r = mid-1
                ans = mid
                print("ans" , ans)  
            elif(k > B):
                l = mid+1
            
            
        return ans

  
print(books(A,B))