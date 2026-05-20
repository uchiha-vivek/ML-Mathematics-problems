# invert the binary tree
from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    


class BinaryTree:
    def __init__(self):
        self.root=None
    
    def invert(self,node):
        if node is None:
            return None
        
        self.invert(node.left)
        self.invert(node.right)
        node.left,node.right = node.right,node.left
        return node
    
    def bfs(self,root):
        if not root:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.data,end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
if __name__=="__main__":
    tree = BinaryTree()
    tree.root = Node(4)
    tree.root.left = Node(2)
    tree.root.right = Node(5)
    print("Normal BFS")
    tree.bfs(tree.root)
    tree.invert(tree.root)
    print(" ")
    print("After inversion")
    tree.bfs(tree.root)