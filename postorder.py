class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create the nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# postorder traversal
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

postorder(root)