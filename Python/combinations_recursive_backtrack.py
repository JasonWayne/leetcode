'''https://leetcode.com/problems/combinations/'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        self._combine(n, k, 0, [], results)
        return results

    def _combine(self, n, k, start, temp, results):
        if len(temp) == k:
            results.append(temp[:])
        for i in range(start, n):
            temp.append(i+1)
            self._combine(n, k, i + 1, temp, results)
            temp.pop()
