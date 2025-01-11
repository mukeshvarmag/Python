A=10
def factorial(A):

    fac=1
    for i in range(1,A+1):
        fac=fac*i
    sumA =0
    print(fac)
    while fac>0:
        if(fac%10==0):
            sumA =sumA+1
        fac=fac//10
    return sumA    

print(factorial(A))            