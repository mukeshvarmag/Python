A = 2
B = 5
C = [1, 10]



          

def paint(k, t, ls):

    def possible(time):
        left, count = time, 1
        for l in ls:
            if time < l * t:
                return False

            left -= l * t
            print(left,"left")
            if left < 0:
                count += 1
                left = time - l * t
                print(count,"count")    
        return count <= k

    l, h = 0, sum(ls) * t
    while l < h:
        m = (l + h) // 2
        print(m,"--")
        if possible(m):
            h = m 
        else:
            l = m + 1

    return l % 10000003

print(paint(A,B,C))    