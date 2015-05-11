class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if (m + n) % 2 == 0:
            # true means need to calculate the average of two numbers
            flag = True
            midIndex = (m + n) / 2
        else:
            flag = False
            midIndex = (m + n) / 2 - 0.5
        # index of A while looping
        j = 0;
        # index of B while looping
        k = 0;
        for i in range(m + n):
            if A[j] < B[k]:
                current = A[j]
            else:
                current = B[k]

            if flag == True and i == midIndex:
                if A[j - 1] < B[k -1]:
                    return (B[k-1] + current) / 2
                else:
                    return (A[j-1] + current) / 2
            if flag == False and i == midIndex:
                return current

            if A[j] < B[k]:
                j += 1
            else:
                k += 1

def test():
    A = [1, 2, 3, 5]
    B = [1.5, 2.5, 3.5, 4]
    sol = Solution()
    res = sol.findMedianSortedArrays(A, B)
    print(res)
