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
    [4, 0, 3],
    [6, 2, 8]
]

possible_move_row = [0,0,-1,1]
possible_move_col = [-1,1,0,0]


class Node:
    def __init__(self, puzzle, parent=None):
        self.board = puzzle
        self.parent = parent

    def __lt__(self, other):
        """Define comparison for heapq (priority queue)."""
        return self.board.f < other.board.f  # Compare based on f-cost

class Puzzle:
    def __init__(self, board, x, y,g=0, h=0):
        self.board = board
        self.x = x
        self.y = y
        self.g = g  # Cost from the start node
        self.h = h  # Heuristic (Manhattan distance)
        self.f = g + h  # Total cost (f = g + h)
    
    def is_goal_state(self):
        return self.board == goal
    
    def is_valid(self, x, y):
        return 0 <= x < N and 0 <= y < N
    
    def get_possible_moves(self):
        moves = []
        for i in range(4):
            new_x = self.x + possible_move_row[i]
            new_y = self.y + possible_move_col[i]

            if self.is_valid(new_x, new_y):
                new_board = [row[:] for row in self.board]
                
                new_board[self.x][self.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[self.x][self.y]

                
                q = 1
                h = manhattan_distance(new_board, goal)

                moves.append(Puzzle(new_board, new_x, new_y, q, h))
        return moves

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

def is_lower_priority(queue, item, new_priority):
    """Check if the new priority is lower than the existing one."""
    for priority, existing_item in queue:
        if existing_item == item:
            return new_priority < priority
    return False  # Item does not exist

start_node = Node(Puzzle(initState,1, 1))

def a_star(start):
    open_list = []
    close_list = []


    heapq.heappush(open_list, (0, start))

    while open_list:
        q = heapq.heappop(open_list)

        curr = q[1].board

        print(curr)

        if curr.is_goal_state():
            print(f'Goal state reached at depth x')
            return
        
        successors = curr.get_possible_moves()

        for successor in successors:

            if successor.is_goal_state():
                print(f'Goal state reached at depth x')
                return


            open_exists = any(entry[1] == successor for entry in open_list)

            open_is_lower = is_lower_priority(open_list,successor,successor.f)

            if open_exists == True and open_is_lower == False: continue

            close_exists = any(entry[1] == successor for entry in close_list)
            close_is_lower = is_lower_priority(close_list,successor,successor.f)

            if close_exists == True and close_is_lower == False: continue
            else:
                heapq.heappush(open_list, (successor.f, Node(successor, curr)))

        close_list.append(q)

a_star(start_node)

