# Leetcode 103 

import collections

class Node:
    def __init__(self,value):
        self.val = value 
        self.left = None
        self.right = None

root = Node("1")
root.left = Node("2")
root.right = Node("3")
root.left.left = Node("4")
root.left.right = Node("5")
root.right.left = Node("6")
root.right.right = Node("7")

def zigzag(root):
    res = []

    if root is None:
        return res 

    q = collections.deque()
    q.append(root)
    flag = True 

    while len(q) > 0:
        size = len(q)
        level = [0] * size
        
        if flag == True:
            index = 0
        else:
            index = size - 1 
        
        for i in range(size):

            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            level[index] = node.val
            if flag == True:
                index += 1
            else:
                index -= 1

        flag = not flag 
        res.append(level)
    return res

print(zigzag(root))
