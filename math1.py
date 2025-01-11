A = [2,6]


def hammingDistance(A):
    bits = [0]*64
    digits = 0
    
    for num in A:
        i = 0
        while num > 0:
            bits[i] += num%2
            num= num//2
            i+=1
        digits = max(i, digits)
    ans = 0
    print(bits)
    print(digits)
    for i in range(digits):
        ans += bits[i]*(len(A)-bits[i])
    return (2*ans)%1000000007


print(hammingDistance(A))