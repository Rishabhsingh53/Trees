import collections
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

def LevelOrder(root):
    if root is None:
        return
    res = []
    q = collections.deque()
    
    q.append(root)
    
    while len(q) > 0:
        size = len(q)
        level = []
        
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.value)
        res.append(level)
    return res

print(LevelOrder(root))