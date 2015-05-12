class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        convert = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        strings = list()
        for number in digits:
            strings.append(convert[int(number)])
        result_pool = []
        for char_set in strings:
            temp = []
            for c in char_set:
                if result_pool:
                    for e in result_pool:
                        temp.append(e + c)
                else:
                    temp.append(c)
            result_pool = temp
        return result_pool
                    
        
