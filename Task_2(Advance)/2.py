class Solution(object):
    def findNumbers(self, nums):
        c = 0
        for i in nums:
            i = str(i)
            a = len(i)
            if a%2==0:
                c+=1
        return c
        