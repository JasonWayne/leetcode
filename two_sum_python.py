class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		dic = {}
		for i in range(len(num)):
			try:
				index1 = dic[target - num[i]]
				index2 = i
				if index1 < index2:
					return (index1+1, index2+1)
				else:
					return (index2+1, index1+1)
			except:
				dic[num[i]] = i
				
def test():
	num = [-3, 4, 3, 34, 3,43]
	target = 0
	sol = Solution()
	res = sol.twoSum(num, target)
	print(res)
