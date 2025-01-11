

A = 2
B = 3
C = 3


def pow(x, n, d):
        
    res = 1 % d 
    # Cover case d == 1
    while n > 0:
        if n & 1:   # Odd?
            res = (res * x) % d
            
        x = x**2 % d
        n >>=1
        
    return res
print(pow(A,B,C))    
