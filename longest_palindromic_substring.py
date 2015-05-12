class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	if s is None:
    		return None
    	cur_longest_string = None
    	cur_longest_length = 0
    	for i in range(len(s) - 1):
    		for j in range(i + 1, len(s)):
    			if j - i <= cur_longest_length:
    				continue
    			if self.isPalindrome(s[i:j]):
    				cur_longest_string = s[i:j]
    				cur_longest_length = j - i
    	return cur_longest_string

    def isPalindrome(self, s):
		for i in range(len(s) / 2):
			if s[i] != s[len(s) - 1 - i]:
				return False
		return True


if __name__ == "__main__":
	# this is a very naive solution and got TLE error
	# try use Manacher's algorithm 
	# http://en.wikipedia.org/wiki/Longest_palindromic_substring
	# https://leetcode.com/discuss/28791/manacher-algorithm-in-python-o-n
 	solution = Solution()
 	assert solution.longestPalindrome('abacb') == 'aba'
 	assert solution.longestPalindrome('abcbad') == 'abcba'
 	assert solution.longestPalindrome('') == None
