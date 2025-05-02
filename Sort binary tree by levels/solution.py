"""Sort binary tree by levels"""

def tree_by_levels(node):
    """main function which sort binary tree by levels"""
    if not node:
        return []

    result = []
    queue = [node]

    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        result.append(node.value)

    return result
