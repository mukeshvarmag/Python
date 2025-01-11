words= ["This", "is", "an", "example", "of", "text", "justification."]
L=16
B=[]
C=""

for i in range(len(words)):
    C=C+(words[i])+" "
    if len(C)<=L:
        B.append(C)

        break  
        
print(C)