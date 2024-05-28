class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None

root = Node("F")
root.left = Node("D")
root.right = Node("J")
root.left.left = Node("B")
root.left.right = Node("E")
root.right.left = Node("G")
root.right.right = Node("K")
root.left.left.left = Node("A")
root.left.left.right = Node("C")
root.right.left.right = Node("I")
root.right.left.right.left = Node("H")

def levelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
        # Print the front of the queue and remove it
        print(queue[0].value)
        node = queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        
levelOrder(root)