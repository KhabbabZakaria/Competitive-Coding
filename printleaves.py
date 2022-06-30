class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BST(10)
tree.left = BST(4)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.right = BST(5)
tree.right = BST(17)
tree.right.right = BST(19)
tree.right.right.left = BST(18)


def printleaves(tree, array):
    if tree is None:
        return
    elif tree.left is None and tree.right is None:
        array.append(tree.value)
    else:
        printleaves(tree.left, array)
        printleaves(tree.right, array)


array = []
printleaves(tree, array)
print(array)




