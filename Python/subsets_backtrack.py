class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self._subsets(nums, 0, [], results)
        return results

    def _subsets(self, nums, start, sub, subs):
    	subs.append(sub[:])
    	for i in range(start, len(nums)):
    		sub.append(nums[i])
    		self._subsets(nums, i + 1, sub, subs)
    		sub.pop()
