class Solution(object):
    def subsets(self, nums):
        def backtrack(index = 0):
            subsets.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        subset, subsets = [], [] 
        backtrack()
        return subsets