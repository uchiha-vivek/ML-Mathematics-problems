# create a binary tree and show me all the standard traversals

class Node:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
    
    
    # preorder traversal
    def preorder(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    #postorder traversal
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")


if __name__=="__main__":
    tree= BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(7)
    print("Inorder:")
    tree.inorder(tree.root)
    print(" ")
    print("Preorder:")
    tree.preorder(tree.root)
    print(" ")
    print("Postorder: ")
    tree.postorder(tree.root)
    
    