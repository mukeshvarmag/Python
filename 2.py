n=int(input())
A = []
# iterating till the range
for i in range(0,n):
    ele = int(input())

    A.append(ele) # adding the element

B = []
# iterating till the range
for i in range(0,n):
    ele = int(input())

    B.append(ele) # adding the element



def sub(a,b):
	x=a-b
	return x

for i in range(0,n):
	y=[]
	for j in range(0,n):
		t=sub(A[i],B[j])
		if t<0:
		  t=t*(-1)
		y.append(t)

	if i==0:
		y[i]=y[i]
	if i>0:
		if y[i]>y[i-1]:
			y[i]=y[i-1]
			 

		
	

for i in range(0,n-1):
	x=sub(A[i],B[i])    
	if x<0:
		x=x*(-1)
	if i==0:
		sum=0
	sum=sum+x
print(sum)	
	