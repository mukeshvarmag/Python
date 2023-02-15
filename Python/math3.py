A="28"
base = ord("A")-1

result = 0
multiplicator = 1
for char in A[::-1]:
    result += (ord(char) - base) * multiplicator
    multiplicator *= 26

print(chr(65),chr(66))


