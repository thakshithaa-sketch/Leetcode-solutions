class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=1
        for i in nums:
            a=a*i
        return (a)