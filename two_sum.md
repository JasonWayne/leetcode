>Given an array of integers, find two numbers such that they add up to a specific target number.<BR><br>
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.<br><br>
You may assume that each input would have exactly one solution.<br><br>
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

##审题：
很容易因为题目中给的示例输入（全部为正，有序等）而给出错误的解答。本题有几点注意：
1. 给的不是一个有序的列表
2. 给的数并不一定都为正
3. 要返回的索引值并不是原来的索引值，而是加1以后的值

##方案一：
```Python
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
```
