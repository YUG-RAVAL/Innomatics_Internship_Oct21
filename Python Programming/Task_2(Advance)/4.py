class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a = []
        for i in range(0,len(nums)):
            c = 0
            for j in range(0,len(nums)):
                if nums[j]<nums[i]:
                    c+=1
            a.append(c)
        return a