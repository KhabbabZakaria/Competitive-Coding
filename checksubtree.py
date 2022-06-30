def preorder(tree, array):
    if tree is None:
        return
    else:
        array.append(tree.value)
        preorder(tree.left, array)
        preorder(tree.right, array)


def popnotpresent(array1, array2):
    import copy
    array1_temp = copy.copy(array1)
    rest = []
    for e in array1:
        if e not in array2:
            rest.append(e)
            array1_temp.remove(e)
    return array1_temp, rest



def ifsubtree(tree1, tree2):
    elements1 = []
    preorder(tree1, elements1)
    elements2 = []
    preorder(tree2, elements2)
    if elements1 == elements2:
        return True
    elif len(elements1)> len(elements2):
        if elements2 in elements1:
            return True
        else:
            elements1_2, rest = popnotpresent(elements1, elements2)
            if elements1_2 == elements2 and max(rest) < elements1[0] and elements1[0]==elements2[0]:
                return True
        return False
    else:
        if elements1 in elements2:
            return True
        else:
            elements2_1, rest = popnotpresent(elements2, elements1)
            if elements2_1 == elements2 and max(rest) < elements1[0] and elements1[0]==elements2[0]:
                return True
        return False

    
    



class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree1 = BST(10)
tree1.left = BST(4)
tree1.left.left = BST(2)
tree1.left.left.left = BST(1)
tree1.left.right = BST(5)
tree1.right = BST(17)
tree1.right.right = BST(19)
tree1.right.right.left = BST(18)

tree2 = BST(10)
tree2.right = BST(17)
tree2.right.right = BST(19)
tree2.right.right.left = BST(18)

#print(ifsubtree(tree1, tree2))



tree = BST(10)
tree.left = BST(4)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.right = BST(5)
tree.right = BST(18)
tree.right.right = BST(19)
tree.right.left = BST(17)
