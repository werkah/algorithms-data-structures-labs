class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),


def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)


root = Node(15)
root.left = Node(6)
root.right = Node(18)
root.right.left=Node(17)
root.left.left = Node(3)
root.left.left.left=Node(2)
root.left.left.right=Node(4)
root.left.right = Node(7)
root.left.right.right = Node(13)
root.left.right.right.left = Node(9)
root.right.right=Node(20)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)