class Solution(object):
    def maxProduct(self, nums):
        nums = sorted(nums)
        a = (nums[-1]-1)*(nums[-2]-1)
        return a