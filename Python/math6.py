A=998

def reverse(A):

    sgn = -1 if A < 0 else 1
    A = abs(A)
    string = str(A)
    reverse = string[::-1]
    result = int(reverse)
    if result > 2**31 - 1:
        return 0
    return sgn * result    
                        
   

print(reverse(A))    