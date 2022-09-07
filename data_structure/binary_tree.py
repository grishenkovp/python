class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res

    # Binary Search Tree (BST)
    def find_val(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + " Not Found"
            return self.left.find_val(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " Not Found"
            return self.right.find_val(val)
        else:
            print(str(self.data) + ' is found')


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorder_traversal(root))
print(root.preorder_traversal(root))
print(root.postorder_traversal(root))
print(root.find_val(140))
print(root.find_val(14))
