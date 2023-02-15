import sys

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
def minimize(A, B, C):
    i= 0
    j = 0
    k = 0
    diff = sys.maxsize
    print(diff)
    while i < len(A) and j < len(B) and k < len(C):
        mini = min(A[i], B[j], C[k])
        maxi = max(A[i], B[j], C[k])
        if maxi-mini < diff:
            diff = maxi- mini
        if diff == 0:
            return 0
        if A[i] == mini:
            i += 1
        elif B[j] == mini:
            j += 1
        else:
            k += 1
    return diff
print(minimize(A,B,C))   