def bfs_recursive(graph, current_level, visited):
    if not current_level:
        return
    
    next_level = []
    for node in current_level:
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            next_level.extend(graph[node])
    
    
    bfs_recursive(graph, next_level, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
print("BFS without Queue & Node:")
bfs_recursive(graph, ['A'], visited)
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def bfs_with_queue(start_node):
    queue = deque([start_node])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node.value, end=" ")
            visited.append(node)
            for child in node.children:
                if child not in visited:
                    queue.append(child)


root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)

print("\nBFS with Queue & Node:")
bfs_with_queue(root)
