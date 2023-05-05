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
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        i, j = node.state.index(0) // 3, node.state.index(0) % 3
        new_i, new_j = i + dx, j + dy
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = node.state[:]
            new_state[i * 3 + j], new_state[new_i * 3 + new_j] = new_state[new_i * 3 + new_j], new_state[i * 3 + j]
            neighbors.append(Node(new_state))
    return neighbors


def heuristic(node, goal):
    """
    Given a node and the goal node, return an estimate of the cost of the cheapest
    path from the current node to the goal node.
    """
    return sum(abs(node.state.index(i) // 3 - goal.state.index(i) // 3) +
               abs(node.state.index(i) % 3 - goal.state.index(i) % 3) for i in range(1, 9))


def astar_search(start, goal):
    """
    Given the start and goal nodes, return the optimal path from the start node to
    the goal node using the A* search algorithm.
    """
    open_set = [start]
    closed_set = []
    nodes_expanded = 0
    while open_set:
        current_node = min(open_set, key=lambda node: node.f)
        if current_node.state == goal.state:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            path.reverse()
            return path, nodes_expanded
        open_set.remove(current_node)
        closed_set.append(current_node)
        nodes_expanded += 1
        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            tentative_g_score = current_node.g + 1
            tentative_h_score = heuristic(neighbor, goal)
            if any(neighbor.state == node.state and tentative_g_score >= node.g for node in closed_set):
                continue
            if not any(neighbor.state == node.state and tentative_g_score < node.g for node in open_set):
                neighbor.parent = current_node
                neighbor.g = tentative_g_score
                neighbor.h = tentative_h_score
                neighbor.f = neighbor.g + neighbor.h
                open_set.append(neighbor)
    return None


start = Node([2, 3, 6, 1, 5, 0, 4, 7, 8])
goal = Node([1, 2, 3, 4, 5, 6, 7, 8, 0])
path, nodes_expanded = astar_search(start, goal)
if path is not None:
    for i, state in enumerate(path):
        print("Node", i)
        print(state.state[0:3])
        print(state.state[3:6])
        print(state.state[6:9])
    print("Final cost:", nodes_expanded)
else:
    print("No solution found.")