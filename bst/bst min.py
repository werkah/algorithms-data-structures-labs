
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def find_min_in_BT(root):
    if root is None:
        return float('inf')
    res = root.data
    lres = find_min_in_BT(root.left)
    rres = find_min_in_BT(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res


if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)

    # Function call
    print("minimum element is",find_min_in_BT(root))

