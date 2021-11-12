class Solution(object):
    def shuffle(self, nums, n):
        a = nums[:n:]
        b = nums[n::]
        c = []
        for i in range(0,n):
            c.append(a[i])
            c.append(b[i])
        
        return c