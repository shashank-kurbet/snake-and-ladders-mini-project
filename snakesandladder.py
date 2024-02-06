class QueueEntry(object):
    def __init__(self, v=0, dist=0, path=[]):
        self.v = v
        self.dist = dist
        self.path = path


def getMinDiceThrows(move, N):
    visited = [False] * N
    queue = []
    visited[0] = True
    queue.append(QueueEntry(0, 0, [0]))  # Start at square 0

    while queue:
        qe = queue.pop(0)
        v = qe.v

        if v == N - 1:
            return qe.dist, qe.path  # Return distance and path when reaching the final square

        j = v + 1
        while j <= v + 6 and j < N:
            if visited[j] is False:
                a = QueueEntry()
                a.dist = qe.dist + 1
                visited[j] = True
                a.v = move[j] if move[j] != -1 else j
                a.path = qe.path + [a.v]  # Update the path
                queue.append(a)

            j += 1

    return -1, []  # Return -1 if no path is found


N = 100
moves = [-1] * N

# Ladders
moves[1] = 38
moves[4] = 14
moves[9] = 31
moves[21] = 42
moves[28] = 84
moves[51] = 67
moves[72] = 91
moves[80] = 99

# Snakes
moves[62] = 19
moves[64] = 60
moves[98] = 79
moves[17] = 7
moves[95] = 75
moves[87] = 36
moves[54] = 34
moves[93] = 73

min_distance, path = getMinDiceThrows(moves, N)

if min_distance == -1:
    print("No path found.")
else:
    print("Min Dice throws required:", min_distance)
    print("Path taken:", path)
