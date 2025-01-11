A =   ["2", "1", "+", "3", "*"]
def evalRPN(A):
    stack = []
    for t in A:
        print(stack,t)
        if t not in ["+", "-", "*", "/"]:
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == "+":
                stack.append(l+r)
            elif t == "-":
                stack.append(l-r)
            elif t == "*":
                stack.append(l*r)
            else:
                    # here take care of the case like "1/-22",
                    # in Python 3.x, it returns -1, while in 
                    # but here it should return 0
                if l*r < 0 and l % r != 0:
                    stack.append(l//r+1)
                else:
                    stack.append(l//r)
    return stack.pop()

print(evalRPN(A))