class Solution(object):
    def runningSum(self, nums):
        b = []
        s = 0
        for i in range(0,len(nums)):
            s = s+nums[i]
            b.append(s)
        return b