

class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None



"""
Encodes a tree to a list of strings
"""
def serialize(root):
    result = []
    nodes = [root]
    
    while nodes:
        next_nodes = []
        for n in nodes:
            if n:
                result.append(str(n.val))
                next_nodes.append(n.left)
                next_nodes.append(n.right)
            else:
                result.append("n")
        nodes = next_nodes
    i = len(result) - 1
    while i >= 0 and result[i] == "n":
        i -= 1
    return result[:i+1]


"""
Decodes your encoded data to tree.
"""
def deserialize(data):
    if (not data) or (data[0] == "n"):
        return None

    root = TreeNode(data[0])
    i = 1
    nodes = [root]
    while nodes:
        next_nodes = []
        j = 0
        while (j < len(nodes)) and (i < len(data)):
            if data[i] != "n":
                l = TreeNode(int(data[i]))
                nodes[j].left = l
                next_nodes.append(l)
            i += 1
            if i < len(data):
                if data[i] != "n":
                    r = TreeNode(int(data[i]))
                    nodes[j].right = r
                    next_nodes.append(r)
                i += 1
                j += 1
        nodes = next_nodes
    return root



root = BinaryTreeNode(5)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(8)

print(serialize(root))
