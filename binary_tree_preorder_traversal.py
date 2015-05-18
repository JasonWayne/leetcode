# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
    	result = []
    	stack = []

    	if not root:
    		return result

    	while stack or root:
    		while root:
    			result.append(root.val)
    			stack.append(root)
    			root = root.left
    		root = stack.pop()
    		root = root.right

    	return result
