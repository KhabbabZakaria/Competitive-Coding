def hasPath(root, arr, x):
     
    # if root is None there is no path
    if root is None:
        return False
     
    # push the node's value in 'arr'
    arr.append(root.value)
    print(root.value)
     
    # if it is the required node
    # return true
    if (root.value == x):    
        return True
     
    # else check whether the required node
    # lies in the left subtree or right
    # subtree of the current node
    if (hasPath(root.left, arr, x) or
        hasPath(root.right, arr, x)):
        return True
     
    # required node does not lie either in
    # the left or right subtree of the current
    # node. Thus, remove current node's value 
    # from 'arr'and then return false    
    arr.pop(-1)
    return False
  
 
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

arr = []
if hasPath(tree, arr, 18):
    print(arr)
