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


def printrightsideHelper(tree, array):
    if tree is None:
        return
    else:
        array.append(tree.value)
        printrightsideHelper(tree.left, array)
        printrightsideHelper(tree.right, array)
        

def printrightside(tree):
    array = []
    tree = tree.right
    printrightsideHelper(tree, array)
    return array  
