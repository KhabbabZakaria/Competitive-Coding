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


def countmaxdepth(tree):
    array = []
    num = 0
    countmaxdepthHelper(tree, array, num)
    return max(array)


def countmaxdepthHelper(tree, array, num):
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        num+=1
        array.append(num)
    else:
        num+=1
        countmaxdepthHelper(tree.left, array, num)
        countmaxdepthHelper(tree.right, array, num)
