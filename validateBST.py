class BST():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BST(10)
tree.left =  BST(4)
tree.left.left =  BST(2)
tree.left.left.left =  BST(1)
tree.left.left.right =  BST(3)
tree.right =  BST(15)
tree.right.left =  BST(12)
tree.right.right =  BST(20)

def validateBST(tree):
    minallowed, maxallowed = float('-inf'), float('inf')
    return validateBSTHelper(tree, minallowed, maxallowed)

def validateBSTHelper(tree, minallowed, maxallowed):
    if tree is None:
        return True

    if tree.value <= minallowed or tree.value > maxallowed:
        return  False

    isleftvalid = validateBSTHelper(tree.left, minallowed, tree.value)
    isrightvalid = validateBSTHelper(tree.right, tree.value, maxallowed)
    return isleftvalid and isrightvalid

print(validateBST(tree))
