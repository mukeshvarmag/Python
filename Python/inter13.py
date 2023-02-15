arrive = [ 9, 47, 17, 39, 35, 35, 20, 18, 15, 34, 11, 2, 45, 46, 15, 33, 47, 47, 10, 11, 27 ]
depart =     [32, 82, 39, 86, 81, 58, 64, 53, 40, 76, 40, 46, 63, 88, 56, 52, 50, 72, 22, 19, 38 ]
K=16


def areBookingsPossible(arrive, depart,k):
    n=len(arrive)
 
    ans = []
 

    for i in range(0, n):
        ans.append((arrive[i], 1))
        ans.append((depart[i], 0))
        
 
    # Sort the vector
    ans.sort()
    
    print(ans[0][1])
    curr_active, max_active = 0, 0
 
    for i in range(0, len(ans)):
 
        if ans[i][1] == 1:
            curr_active += 1
            max_active = max(max_active,
                             curr_active)

        else:
            curr_active -= 1

    if ( k >= max_active):
        return 1
    if (K<max_active):
        return 0    

print(areBookingsPossible(arrive,depart,K))    
                       
