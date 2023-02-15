A = "{A,B[C]}"
def prettyJSON(A):
	indent = 0
	res = []
	line = ''
	for x in A:
	    if x in '{[':
	        if line:
	            res.append(line)
	        res.append('\t' * indent + x)
	        line = ''
	        indent += 1
	    elif x in ']}':
	        if line:
	            res.append(line)
	        indent -= 1
	        line = '\t' * indent + x  # Might be followed by ','
	    else:
	        if not line:
	            line = "\t" * indent
	        line += x
	        if x == ",":
	            res.append(line)
	            line = ''
	if line:
	    res.append(line)
	return res
print(prettyJSON(A))    