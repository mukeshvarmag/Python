A="((a + b))"
def checkRedundancy(Str):
     
    # create a stack of characters
    st = []
 
    # Iterate through the given expression
    for ch in Str:
 
        # if current character is close
        # parenthesis ')'

        if (ch == ')'):
            top = st[-1]

 
            # If immediate pop have open parenthesis
            # '(' duplicate brackets found
            flag = True
            print(st)
 
            while (top != '('):
                print(top)
                

                
 
                # Check for operators in expression
                if (top == '+' or top == '-' or
                    top == '*' or top == '/'):
                    flag = False
 
                # Fetch top element of stack
                top = st[-1]
                st.pop()
        

            if (flag == True):
                return 1
 
        else:
            st.append(ch) # append open parenthesis '(',
                          # operators and operands to stack
    return 0
print(checkRedundancy(A))    