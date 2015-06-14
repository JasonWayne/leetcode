# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append((root, 0))
                root = root.left
            root, state = stack.pop()
            if state == 0:
                if root.right:
                    # 1 means the right child of the node has been visited
                    stack.append((root, 1))
                    root = root.right
                else:
                    result.append(root.val)
                    root = None
            else:
                result.append(root.val)
                root = None
        return result
        
