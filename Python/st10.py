A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trap(A):

    water=0
    stack=[]
    for i in A:
        print(stack,i)
        if stack and stack[0]<=i:
            h=stack[0]
            while stack:
                n=stack.pop()
                water=water+(h-n)
        stack.append(i)
    h=stack.pop()
    
    while stack:
        n=stack.pop()
        
        if  n>h:
            h=n
            continue
        water=water+(h-n)
    return water
print(trap(A))    