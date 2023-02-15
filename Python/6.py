fhand = open("3.txt")
count = 0
for line in fhand:
    #print(line)
    line = line.rstrip()
    #print(line)
    if line == "": continue
        
    words = line.split()
    if   words[0] !="From": continue
        
    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")