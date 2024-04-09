class TreeNode:
    def __init__(self, value: int):
        self.data = value;
        self.left = None
        self.right = None

def preorder(root: TreeNode):
    if root != None:
        print(root.data, end="  ")
        preorder(root.left)
        preorder(root.right)

def inorder(root: TreeNode):
    if root != None:
        inorder(root.left)
        print(root.data, end="  ")
        inorder(root.right)

def postorder(root: TreeNode):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="  ")



#  Driver Code

# Creating Nodes   
root = TreeNode(60)
n1 = TreeNode(40)
n2 = TreeNode(80)
n3 = TreeNode(20)
n4 = TreeNode(30)
n5 = TreeNode(70)
n6 = TreeNode(90)

# Linking Nodes
root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n2.left = n5
n2.right = n6



print("Pre-Order:  ", end=" ")
preorder(root)
print("\nIn-Order:   ", end=" ")
inorder(root)
print("\nPost-Order: ", end=" ")
postorder(root)