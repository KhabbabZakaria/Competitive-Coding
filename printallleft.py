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


def preorder(tree, array):
    if tree is None:
        return
    else:
        array.append(tree.value)
        preorder(tree.left, array)
        preorder(tree.right, array)

def printallleft(array):
    array = []
    preorder(tree, array)
    root_or_right = array[0]
    idx = 1
    result = []
    while idx<len(array):
        if array[idx]<root_or_right:
            result.append(array[idx])
        else:
            root_or_right = array[idx]
        idx+=1
    return result


print(printallleft(tree))




