class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root,data)
    
    def _insert_recursive(self,current_node,data):
        if data< current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left,data)
        elif data> current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right,data)
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)


if __name__=="__main__":
    bst = BinarySearchTree()
    elements  = [10,5,15,3,7,12,18]
    for elem in elements:
        bst.insert(elem)
    print("Traversal :")
    bst.inorder(bst.root)
    print()