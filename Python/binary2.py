A=[5,7,7,8,8,10]
B=8
def searchRange(A, B):
        
    def searchFirst(arr,start,end,element):
        ans = -1
        while start<=end:
            mid = start + (end-start)//2
            print(mid)
            if arr[mid]==element:
                ans=mid
                end=mid-1
                
            elif arr[mid]<element:
                start = mid + 1
            else:
                end = mid - 1
        return ans
            
    def searchLast(arr,start,end,element):
        ans = -1
        while start<=end:
            mid = start + (end-start)//2
            if arr[mid]==element:
                ans=mid
                start=mid+1
            elif arr[mid]<element:
                start = mid + 1
            else:
                end = mid - 1
        return ans
        
    return [searchFirst(A,0,len(A)-1,B),searchLast(A,0,len(A)-1,B)]


print(searchRange(A,B))    