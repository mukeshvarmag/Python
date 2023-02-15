arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]

n = len(arr)


    
leftMax = [None] * n 
 
leftMax[0] = float('-inf')  

  
 
for i in range(1, n):  
    leftMax[i] = max(leftMax[i-1], arr[i-1])  
  
   
print(leftMax)   
rightMin = float('inf')  
  
  
for i in range(n-1, -1, -1):  
       
    
    if leftMax[i] < arr[i] and rightMin > arr[i]:  
        print("1")

  
  
    rightMin = min(rightMin, arr[i])  

  


