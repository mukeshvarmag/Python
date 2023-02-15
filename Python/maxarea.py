A = [2, 1, 5, 6, 2, 3]

def largestRectangleArea(A):
    height = A
    height.append(0)


    stack = [-1]

    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            print(height[stack[-1]],i)
            h = height[stack.pop()]
            
            
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    return ans
print(largestRectangleArea(A))    