B=3
def printPattern(A):
 
    B = A * 2 - 1
    result = [[0 for x in range(B)]
                 for y in range(B)]
         
    # Fill the values
    for i in range(B):
        for j in range(B):
            if(abs(i - (B // 2)) >
               abs(j - (B // 2))):
                result[i][j] = abs(i - (B // 2)) + 1
            else:
                result[i][j] = abs(j - (B // 2)) + 1
             
    # Print the array
    return result

print(printPattern(B))