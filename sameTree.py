class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
p = Node(1)
q = Node(1)
p.left = Node(2)
q.left = Node(2)
p.right = Node(3)
q.right = Node(3)

def answer(p , q):
    if p is not None and q is None:
        return False
    if p is None and q is not None:
        return False 
    if p and q and p.val != q.val:
        return False
    if p and q and p.val == q.val:
        return answer(p.left,q.left) and answer(p.right,q.right)
print(answer(p,q))