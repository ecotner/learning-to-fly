class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        for n in range(len(nums)//2):
            total += nums[2*n]
        return total
