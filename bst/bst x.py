class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def iterativeSearch(root, x):
    if (root == None):
        return False
    nodeStack = []
    nodeStack.append(root)
    while (len(nodeStack)):
        node = nodeStack[0]
        if (node.data == x):
            return True
        nodeStack.pop(0)
        if (node.right):
            nodeStack.append(node.right)
        if (node.left):
            nodeStack.append(node.left)
    return False


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

if iterativeSearch(root, 6):
    print("Found")
else:
    print("Not Found")

