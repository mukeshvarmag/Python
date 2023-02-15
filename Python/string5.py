A = "the sky is blue"


def solve(A):
    return ' '.join(A.strip().split()[::-1])
print(solve(A))    