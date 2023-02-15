A=5

class Direction(object):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


def generateMatrix(A):
    result = [[0] * A for _ in range(A)]
    t, b, l, r = 0, A - 1, 0, A - 1 
    direction = Direction.EAST
    lastN = 1
    while t <= b and l <= r:
        if direction is Direction.EAST:
                # A[t][l:r + 1]
            for col in range(l, r + 1):
                result[t][col] = lastN
                lastN += 1
            t += 1
        elif direction is Direction.SOUTH:
                # A[r][t:b + 1]
            for row in range(t, b + 1):
                result[row][r] = lastN
                lastN += 1
            r -= 1
        elif direction is Direction.WEST:
                # reversed(A[b][l:r + 1])
            for col in reversed(range(l, r + 1)):
                result[b][col] = lastN
                lastN += 1
            b -= 1
        elif direction is Direction.NORTH:
            for row in reversed(range(t, b + 1)):
                result[row][l] = lastN
                lastN += 1
            l += 1
        direction = (direction + 1) % 4
    return result

print(generateMatrix(A))    