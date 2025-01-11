A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

def printRepeating(arr):
 

 
    for i in range(len(A)):
 
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
            print(abs(arr[i]), end=" ")


print(printRepeating(A))            