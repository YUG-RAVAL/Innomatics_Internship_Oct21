class Solution(object):
    def numIdenticalPairs(self, nums):
        c=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    c+=1
                else:
                    continue
        return c