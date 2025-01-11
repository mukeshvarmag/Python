
A="ababda"
    
def solve(A):
    s = set()
    stack = []
    ans = []
    print(s)
        
    for i in A:
        if i not in s:
            s.add(i)
            stack.append(i)
            ans.append(stack[0])
        else:
            if i in stack:
                stack.remove(i)
            if stack:
                ans.append(stack[0])
            else:
                ans.append('#')
                
    return "".join(ans)
print(solve(A))    