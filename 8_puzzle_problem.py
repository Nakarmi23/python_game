from itertools import chain
import heapq

N = 3

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
initState = [
    [1, 7, 5],
    [0, 4, 3],
    [6, 2, 8]
]

possible_move_row = [0,0,-1,1]
possible_move_col = [-1,1,0,0]


class Node:
    def __init__(self, puzzle, parent=None, x=0, y=0):
        self.board = puzzle
        self.parent = parent
        self.x = x
        self.y = y

class Puzzle:
    def __init__(self, board):
        self.board = board
    
    def is_goal_state(self):
        return self.board == self.goal
    
    def is_valid(self, x, y):
        return 0 <= x < N and 0 <= y < N
    
    def __repr__(self):
        temp = []
        for row in self.board:
            temp.append(" ".join(map(str, row)))
        temp.append("---------")
        return "\n".join(temp)

def manhattan_distance(initState, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if initState[i][j] != 0:
                x,y = divmod(list(chain(*goal)).index(initState[i][j]), 3)
                distance += abs(x-i) + abs(y-j)

    return distance



start_node = Node(Puzzle(initState))

def a_star(start):
    open_list = []
    close_list = []

    heapq.heappush(open_list, (0, start))

    while open_list:
        q = heapq.heappop(open_list)



print(start_node)

