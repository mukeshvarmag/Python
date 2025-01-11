A="/a/./b/../../c/"
def simplifyPath(A):
    dirs = A.split('/')
    print(dirs)
    result = []
    for c in dirs:
        if c == '' or c == '.':
            continue
        elif c == '..':

            if len(result)>0:
                result.pop()
        else:
            result.append(c)
    print(result)        
    return '/'+'/'.join(result)
print(simplifyPath(A))    