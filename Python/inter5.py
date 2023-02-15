from functools import cmp_to_key

A= [12,121]


def largestNumber(A):

	A = map(str, A)
    
	key_A = cmp_to_key(lambda a,b: 1 if a+b>=b+a else -1)
	res = ''.join(sorted(A, key= key_A, reverse=1))

    
	    
	res = res.lstrip('0')
	return res if res else '0'

print(largestNumber(A))    