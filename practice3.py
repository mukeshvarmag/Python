from functools import cmp_to_key

A= [8,9,60]


def largestNumber(A):

	A = map(str, A)
    
	key_A = cmp_to_key(lambda a,b: 1 if a>=b else -1)
	res = sorted(A, key= key_A, reverse=1)

    
	    
	
	return res if res else '0'

print(largestNumber(A))    