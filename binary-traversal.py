
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)
    
"""
1. Iterative preorder traversal of a binary tree
"""
def preorder(root):

    # base case:
    if root is None:
        return []

    stack = Stack()
    stack.push(root)
    node_vals = []

    while stack.isEmpty() == False:
        node = stack.pop()
        node_vals.append(node.val)

        if node.right is not None:
            stack.push(node.right)
        if node.left is not None:
            stack.push(node.left)
    return node_vals
            
"""
2. Reconstruct Binary Tree
"""
def reconstructBT(preorder, inorder):
    preorder.reverse()
    return reconstructBT_helper(preorder, inorder)

def reconstructBT_helper(preorder, inorder):
    if preorder == [] or inorder == []:
        return None

    node = BinaryTreeNode(preorder.pop())
    index = inorder.index(node.val)

    node.left = reconstructBT_helper(preorder, inorder[:index])
    node.right = reconstructBT_helper(preorder, inorder[index + 1:])

    return node
    

"""
3. Convert Binary Search Tree
"""
total = 0
def convertBSTtoGST(root):
    global total
    total = 0
    result = BSTtoGST_helper(root)
    return result

def BSTtoGST_helper(root):

    # base case
    if root == None or root.val == None:
        return

    BSTtoGST_helper(root.right)

    global total

    total += root.val

    root.val = total

    BSTtoGST_helper(root.left)

    return root
