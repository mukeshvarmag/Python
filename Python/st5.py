A = [4, 5, 2, 10, 8]
def prevSmaller(A):
    stack = []
    result = []
    for num in A:
        print(stack)
            # see of there's integer smaller than num in the stack
        while stack and stack[-1] >= num:
            stack.pop()
        if stack:  # found the smaller integer
            result.append(stack[-1])
        else:  # stack is empty, smaller integer wasn't found
            result.append(-1)
        stack.append(num)  # push current num to the stack
    return result
                
print(prevSmaller(A))