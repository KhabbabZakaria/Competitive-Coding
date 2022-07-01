# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    global maxdia
    maxdia = 0
    global tempdia
    tempdia = 0
    binaryTreeDiameterHelper(tree)
    return  maxdia

def binaryTreeDiameterHelper(tree):
    global maxdia
    global tempdia
    if tree is None:
        if tempdia>maxdia:
            maxdia = tempdia
        return
    if tree.left is not None and tree.right is not None and tree.left.left is not None and tree.left.right is not None and  tree.right.left is not None and tree.right.right is not None :
        if tempdia>maxdia:
            maxdia = tempdia
        tempdia = 4
    elif tree.left is not None and tree.right is not None:
        if tempdia>maxdia:
            maxdia = tempdia
        tempdia = 2
    elif tree.left is not None and tree.right is None:
        tempdia+=1
    elif tree.left is None and tree.right is not None:
        tempdia+=1
    binaryTreeDiameterHelper(tree.left)
    binaryTreeDiameterHelper(tree.right)
