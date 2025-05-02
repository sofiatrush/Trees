"""Delete Node in a BST """
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """Class for solution"""

    def delete_node(self, root, key: int):
        """
        main function which delete node in binary search tree
        """
        if not root:
            return root

        if key > root.val:
            root.right = self.delete_node(root.right, key)
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key == root.val:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            min_node = root.right
            while min_node.left:
                min_node = min_node.left

            root.val = min_node.val
            root.right = self.delete_node(root.right, root.val)

        return root

# root = TreeNode(5)
# root.left = TreeNode(3, TreeNode(2), TreeNode(4))
# root.right = TreeNode(6, None, TreeNode(7))
# solution = Solution()
# new_root = solution.deleteNode(root, 3)
