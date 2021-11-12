class Solution(object):
    def xorOperation(self, n, start):
        res = start
        for i in range (1,n):
            res ^= (start + i * 2)
        return res