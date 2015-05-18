# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    _answer = []

    def inorderTraversal(self, root):
        self.inorderTraversal(root.left)
        if root.value != '#':
        	self._answer.append(root.value)
        else:
        	return None
        self.inorderTraversal(root.right)


if __name__ == "__main__":
	sol = Solution()
	assert sol.inorderTraversal([1, '#', 2, 3])
