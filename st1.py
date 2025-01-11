A="(()()(())("
def solve(A):
    st = []
    i = 0
    while i < len(A):
        if A[i] == '(':
            st.append(A[i])
        else:
            if not st:
                return 0
            print(st.pop())
        i += 1
        
    return 1 if not st else 0
print(solve(A))    