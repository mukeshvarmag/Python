import numpy as np
A =( 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 )
B =9
def kthsmallest(A):
    
	arr=np.asarray(A)
   
    
	return sorted(arr)

def sor(A,B):
    C=kthsmallest(A)
    return C[B-1]
print(sor(A,B))


