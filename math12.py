from math import factorial as f
def nCr(n,r):
    return f(n)//(f(r)*f(n-r))

A=2
B=2
def uniquepath(A,B):
    return nCr((A+B-2),A-1)    
print(uniquepath(A,B))    