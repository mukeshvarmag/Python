
n = int(input("Enter :"))
lst = []
for i in range(n):
    ele = int(input())
    lst.append(ele)


def max(A,B):
  if A>B:
    return A
  else:
    return B

def min(A,B):
  if A<B:
    return A
  else:
    return B


mx=max(lst[0],lst[1]) 

secondmax=min(lst[0],lst[1]) 
  


 



n =len(lst)

for i in range(2,n): 

    if lst[i]>mx: 

        secondmax=mx

        mx=lst[i] 

    elif lst[i]>secondmax and mx != lst[i]: 

        secondmax=lst[i]
 

print(secondmax)
