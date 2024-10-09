class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0 
        self.h = 0  
        self.f = 0  

def astar(maze, start, end):

    start_node = Node(start)
    end_node = Node(end)

    open_list = [start_node]
    closed_list = []

    while open_list:
        current_node = open_list[0]
        current_index = 0
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

       
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 

        neighbors = [
            (0, -1), (0, 1),  
            (-1, 0), (1, 0)   
        ]

        for move in neighbors:
            neighbor_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if neighbor_pos[0] < 0 or neighbor_pos[0] >= len(maze) or neighbor_pos[1] < 0 or neighbor_pos[1] >= len(maze[0]):
                continue

            if maze[neighbor_pos[0]][neighbor_pos[1]] != 0:
                continue

            neighbor_node = Node(neighbor_pos, current_node)

            
            if any(closed_neighbor.position == neighbor_node.position for closed_neighbor in closed_list):
                continue

            neighbor_node.g = current_node.g + 1
            neighbor_node.h = abs(neighbor_node.position[0] - end_node.position[0]) + abs(neighbor_node.position[1] - end_node.position[1])
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(open_node.position == neighbor_node.position and open_node.g <= neighbor_node.g for open_node in open_list):
                continue

            open_list.append(neighbor_node)

    return None 

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(maze, start, end)
print("Path:", path)
