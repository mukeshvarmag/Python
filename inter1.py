def shortestPath(p1, p2):
      
    # dx is total horizontal
    # distance to be covered
    dx = abs(p1[0] - p2[0])
      
    # dy is total vertical
    # distance to be covered
    dy = abs(p1[1] - p2[1])
      
    # required answer is
    # maximum of these two
    return max(dx, dy)
      
# Function to return the minimum steps
def coverPoints(sequence, size):
      
    stepCount = 0
      
    # finding steps for each
    # consecutive poin the sequence
    for i in range(size-1):
        stepCount += shortestPath(sequence[i],sequence[i + 1])
          
    return stepCount
  
# For list of integers
# For list of integers
x = []  
  
# For list of strings/chars
y = []  
  
x = [int(item) for item in input("Enter the list items : ").split()]
  
y = [int(item) for item in input("Enter the list items : ").split()]




m = len(x)

arr=[]
for i in range(0,m):
    ele = x[i],y[i]
    arr.append(ele)
 

n = len(arr)
print(coverPoints(arr, n))   