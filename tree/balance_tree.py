# checking if the tree is balanced or not


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def max_depth(self,node):
        if node is None:
            return 0
        
        left_depth  = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        return max(left_depth,right_depth)+1
        
    
    def check_height(self,node):
        if node is None:
            return True
        
        left_depth = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        # print(left_depth,right_depth)
        balance_condition = abs(left_depth-right_depth) <=1
        if balance_condition and self.check_height(node.left) and self.check_height(node.right):
            return True
        return False


if __name__=="__main__":
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(8)
    tree.root.right = Node(12)
    tree.root.left.left = Node(6)
    print("Maximum depth")
    print(tree.max_depth(tree.root))
    print("")
    print("Tree balance status")
    ans = tree.check_height(tree.root)
    print(ans)