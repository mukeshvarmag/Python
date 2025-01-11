MAX_INT = 2**31 - 1
MIN_INT = -2**31


def atoi(self, A):
	    
	    
	    A = A.strip()
	    i, n = 0, len(A)
	    
	    # Handle sign
	    sign = 1
	    if A[0] == '-':
	        sign = -1
	    if A[0] in '-+':
	        i += 1
	    
	    # Process digits
	    res = 0
	    while i<n:
	        if '0' <= A[i] <= '9':
	            res = 10*res + (ord(A[i]) - 48)
	        else:
	            break
	        i += 1
	    
	    res = sign*res
	    
	    # Make python as dumb as C
	    return max(MIN_INT, min(MAX_INT, res))