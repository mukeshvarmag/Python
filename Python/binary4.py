A=25
def sqrt(A):
        if A == 0:
            return 0
        if A >= 1 and A <= 3:
            return 1
        low = 1
        high = A//2
        
        while low <= high:
            mid = low + (high-low)//2
            if (mid*mid == A):
                return mid
            if (mid*mid < A):
                low = mid+1
                val = mid
            else:
                high = mid-1
        
        return val           


print(sqrt(A))

    

