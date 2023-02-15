s=str(3241)
def solve(s):
    for i in range(len(s) - 2, -1, -1):
        print(i)
        tail = sorted(s[i:])
        print(tail)
        for j in range(len(tail)):
            m = int(s[:i] + tail[j] + ''.join(tail[:j] + tail[j+1:]))
            print(m)
            if m > int(s):
                return m

    return '-1'
print(solve(s))    