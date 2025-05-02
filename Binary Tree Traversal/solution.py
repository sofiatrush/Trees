"""Binary Tree Traversal"""
class Node(object):
    """Class for a Node"""

    def __init__(self, data=None):
        """To initialize a Node."""
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    """Pre-order traversal"""
    if node is None:
        return []
    result = [node.data]
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))
    return result

# In-order traversal
def in_order(node):
    """In-order traversal"""
    if node is None:
        return []
    result = in_order(node.left)
    result.append(node.data)
    result.extend(in_order(node.right))
    return result

# Post-order traversal
def post_order(node):
    """Post-order traversal"""
    if node is None:
        return []
    result = post_order(node.left)
    result.extend(post_order(node.right))
    result.append(node.data)
    return result

# a = Node("A")
# b = Node("B")
# c = Node("C")

# a.left = b
# a.right = c

# print(a.left.data)
# print(a.right.data)

# d = Node("D")
# c.left = d

# print(c.left.data)
