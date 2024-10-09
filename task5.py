class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs_with_stack(start_node):
    stack = []
    visited = []

  
    stack.append(start_node)

    while stack:
        
        current_node = stack.pop()

        if current_node not in visited:
          
            visited.append(current_node)
            print(current_node.value)

            for child in reversed(current_node.children):
                if child not in visited:
                    stack.append(child)

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

print("DFS traversal:")
dfs_with_stack(root)
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
       
        inorder_traversal(node.left)
       
        print(node.value, end=" ")
      
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        
        print(node.value, end=" ")
       
        preorder_traversal(node.left)
       
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
       
        postorder_traversal(node.left)
       
        postorder_traversal(node.right)
        
        print(node.value, end=" ")

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

print("Inorder traversal:")
inorder_traversal(root)  

print("\nPreorder traversal:")
preorder_traversal(root)  
print("\nPostorder traversal:")
postorder_traversal(root)  