"""
https://leetcode.com/problems/subsets-ii/
使用和subsets的recusive backtrack版本相同的做法
对最后的结果进行去重
提交了四次，运行时间68, 76, 84, 148ms，
68ms beats 82%, 148ms beats 1%
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self._subsetsWithDup(nums, 0, [], results)
        results.sort()
        kick = set()
        for i in range(1, len(results)):
            if results[i] == results[i - 1]:
                kick.add(i)
        ret = []
        for i in range(len(results)):
            if i not in kick:
                ret.append(results[i])
        return ret

    def _subsetsWithDup(self, nums, start, temp, results):
        results.append(temp[:])

        for i in range(start, len(nums)):
            temp.append(nums[i])
            self._subsetsWithDup(nums, i + 1, temp, results)
            temp.pop()
        