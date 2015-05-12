class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	# inspired by https://leetcode.com/discuss/21332/python-o-n-2-method-with-some-optimization-88ms
    	start = 0
    	max_length = 1
    	for i in range(len(s)):
    		if i - max_length - 1 >= 0 \
    			and self.isPalindrom(s[i - max_length - 1:i+1]):
    			start = i - max_length - 1
    			max_length = max_length + 2
    			continue
    		if i - max_length >= 0 \
    			and self.isPalindrom(s[i - max_length:i+1]):
    			start = i - max_length
    			max_length = max_length + 1
    	return s[start:start+max_length]

    def isPalindrom(self, s):
    	max_index = len(s) - 1
    	for i in range(len(s) / 2):
    		if s[i] != s[max_index - i]:
    			return False
    	return True


if __name__ == "__main__":
 	solution = Solution()
 	assert solution.longestPalindrome('abacb') == 'aba'
 	assert solution.longestPalindrome('abcbad') == 'abcba'
