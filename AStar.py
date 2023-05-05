class Node:
    def __init__(self, state=None, parent=None, g=0, h=0):
        self.state = state          # the position of the node in the search space
        self.parent = parent        # the parent node of the current node
        self.g = g                  # the cost of the path from the start node to the current node
        self.h = h                  # the heuristic estimate of the cost from the current node to the goal node
        self.f = g + h              # the total cost of the path from the start node to the goal node through the current node


def get_neighbors(node):
    """
    Given a node, return a list of its neighboring nodes that are accessible
    from the current node (i.e., not blocked by obstacles).
    """
    neighbors = []
    # Define the possible moves (UP, DOWN, LEFT and RIGHT) from the current position
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        i, j = node.state.index(0) // 3, node.state.index(0) % 3
        new_i, new_j = i + dx, j + dy
        # Check if the new position is within the boundaries of the search space
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = node.state[:]
            new_state[i * 3 + j], new_state[new_i * 3 + new_j] = new_state[new_i * 3 + new_j], new_state[i * 3 + j]
            # Append the state to the nearest neighbor node
            neighbors.append(Node(new_state))
    return neighbors


def heuristic(node, goal):
    """
    Given a node and the goal node, return an estimate of the cost of the cheapest
    path from the current node to the goal node.
    """
    # Calculate the Manhattan distance between the current position and the goal position for each tile
    # Return the sum of all Manhattan distances as the heuristic cost
    return sum(abs(node.state.index(i) // 3 - goal.state.index(i) // 3) +
               abs(node.state.index(i) % 3 - goal.state.index(i) % 3) for i in range(1, 9))


def astar_search(start, goal):
    """
    Given the start and goal nodes, return the optimal path from the start node to
    the goal node using the A* search algorithm.
    """
    open_set = [start] # List of nodes to be evaluated on
    closed_set = [] # List of nodes that have already been evaluated
    nodes_expanded = 0 # How many nodes were expanded during the search
    while open_set:
        # Selects the node with the lowest total cost (f) from the open set
        current_node = min(open_set, key=lambda node: node.f)
        if current_node.state == goal.state:
            # Reconstructs the path from the start node to the goal node by following parent pointers
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            path.reverse()
            return path, nodes_expanded
        open_set.remove(current_node)
        closed_set.append(current_node)
        nodes_expanded += 1
        # Get neighbors of the current node
        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            # Calculate g and h scores
            tentative_g_score = current_node.g + 1
            tentative_h_score = heuristic(neighbor, goal)
            # Check if neighbor has already been evaluated
            if any(neighbor.state == node.state and tentative_g_score >= node.g for node in closed_set):
                continue
            # Check if the neighbor is not already in the open set, or if it has a better g score
            if not any(neighbor.state == node.state and tentative_g_score < node.g for node in open_set):
                # If the neighbor is not already in the open set, set its parent, g, h, and f scores, and add it to the open set
                neighbor.parent = current_node
                neighbor.g = tentative_g_score
                neighbor.h = tentative_h_score
                neighbor.f = neighbor.g + neighbor.h
                open_set.append(neighbor)
    return None

# Define start and goal configuration:
start = Node([2, 3, 6, 1, 5, 0, 4, 7, 8])
goal = Node([1, 2, 3, 4, 5, 6, 7, 8, 0])

# Find the optimal path with the A* algorithm
path, nodes_expanded = astar_search(start, goal)

# If a solution is found, print the state of each node on the optimal path, and the final cost
if path is not None:
    for i, state in enumerate(path):
        print("Node", i)
        print(state.state[0:3])
        print(state.state[3:6])
        print(state.state[6:9])
    print("Final cost:", nodes_expanded)
else:
    print("No solution found.")