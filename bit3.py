A=5
B=2
def divide(self, A, B):
    if ( A == 0 ):
        return 0
    flag = 1
    if ( ( A > 0 and B < 0 ) or ( A < 0 and B > 0 ) ):
        flag = -1
    quotient = 0
    m = abs(A)
    n = abs(B)
    if ( n == 1 ):
        if ( m > 2147483647 and flag == 1 ):
            return 2147483647
        return (flag * m)
    while ( m >= n ):
        m = m - n
        quotient = quotient + 1
        if ( quotient > 2147483647 and flag == 1 ):
            return 2147483647
       
    return (flag * quotient)