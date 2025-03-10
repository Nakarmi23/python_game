from collections import deque
from copy import deepcopy

class BridgePuzzle:
    def __init__(self, state = None, totalCost = 0):
        if state:
            self.state = state
        else:
            self.state = {
                "Left": {"Flashlight", "Teen", "Young Adult", "Adult", "Elderly", ""},
                "Right": {""},
            }
        self.individualCost = {
            "Teen": 1,
            "Young Adult": 2,
            "Adult": 5,
            "Elderly": 10,
            "": 0,
        }
        self.totalCost = totalCost

        self.possible_actions = [
            # Single person crossing from Right to Left
            ("Teen", "", "<"),
            ("Young Adult", "", "<"),
            ("Adult", "", "<"),
            ("Elderly", "", "<"),

            # Two people crossing from Right to Left
            ("Teen", "Young Adult", "<"),
            ("Teen", "Adult", "<"),
            ("Teen", "Elderly", "<"),
            ("Young Adult", "Adult", "<"),
            ("Young Adult", "Elderly", "<"),
            ("Adult", "Elderly", "<"),

            # Single person returning from Left to Right
            ("Teen", "", ">"),
            ("Young Adult", "", ">"),
            ("Adult", "", ">"),
            ("Elderly", "", ">"),

            # Two people returning from Left to Right
            ("Teen", "Young Adult", ">"),
            ("Teen", "Adult", ">"),
            ("Teen", "Elderly", ">"),
            ("Young Adult", "Adult", ">"),
            ("Young Adult", "Elderly", ">"),
            ("Adult", "Elderly", ">"),
        ]

    
    def is_goal(self):
        goalState = {
            "Left": {""},
            "Right": {"Flashlight", "Teen", "Young Adult", "Adult", "Elderly", ""},
        }

        return self.state == goalState
    
    def is_valid_action(self, action):

        if action not in self.possible_actions:
            return False
        
        
        if action[2] == "<":
            return (action[0] in self.state["Right"]) and (action[1] in self.state["Right"]) and "Flashlight" in self.state["Right"]
        else:
            return (action[0] in self.state["Left"]) and (action[1] in self.state["Left"]) and "Flashlight" in self.state["Left"]
        
    def next_actions(self):
        temp = []
        
        for action in self.possible_actions:
            if self.is_valid_action(action):
                temp.append(action)
        
        return temp
    
    def move(self, action):
        if not self.is_valid_action(action):
            raise Exception("Error: Invalid Action")
        
        self.totalCost = self.totalCost + max(self.individualCost[action[0]], self.individualCost[action[1]])

        from_side = "Right" if action[2] == "<" else "Left"
        to_side = "Left" if action[2] == "<" else "Right"

        self.state[to_side].add("Flashlight")
        self.state[from_side].remove("Flashlight")
        
        self.state[to_side].add(action[0])
        self.state[from_side].remove(action[0])

        if action[1]:
            self.state[to_side].add(action[1])
            self.state[from_side].remove(action[1])

    def __repr__(self):
        leftPeople  = ', '.join(self.state['Left']) if len(self.state['Left']) else "Empty"
        rightPeople  = ', '.join(self.state['Right']) if len(self.state['Right']) else "Empty"
        return f"{leftPeople} ------------- {rightPeople}"
    
# Tree Nodes
class Node:
    def __init__(self, puzzle, parent=None, prev_action=None):
        self.state = puzzle
        self.parent = parent
        self.prev_action = prev_action

def BFS(root):
    visited = set()
    q = deque()
    q.append(root)

    itr = 1

    while q:
        node = q.popleft()
        if str(node.state.state) in visited: 
            continue

        visited.add(str(node.state.state))
        print("Iteration:", itr, node.state)

        if node.state.is_goal():  # if the destination is reached, return distance
            print("Goal State Achieved")
            print(node.state)
            return backtrace(node), node.state.totalCost
        
        for action in node.state.next_actions():
            new_state = BridgePuzzle(deepcopy(node.state.state), node.state.totalCost)
            new_state.move(action)
            new_node = Node(new_state, node, action)
            q.append(new_node)

        itr += 1



def backtrace(node):
    path = []

    while node.parent is not None:
        path.append(node.prev_action)
        node = node.parent

    return list(reversed(path))  # Reverse to get correct order



root = Node(BridgePuzzle())
print(BFS(root))