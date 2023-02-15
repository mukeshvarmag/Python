A=5
def countAndSay(A):
    numbers = [1] #Stores list of numbers
    for i in range(A-1):
        count = 1
        counts = []
        for j in range(len(numbers)):
                # Handle last element case
            if j == len(numbers) - 1: 
                counts.append(count)
                counts.append(numbers[j])
                break
                #Increment count for matching elements
            if numbers[j] == numbers[j+1]:
                count += 1
            else:
                counts.append(count)
                counts.append(numbers[j])
                count = 1
            
        numbers = counts
    return "".join([str(x) for x in numbers])        
print(countAndSay(A))    