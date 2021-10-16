class Solution(object):
    def countBits(self, n):
        a = [0]*(n+1)
        for i in range(n+1):
            a[i] = bin(i).count("1")
        return a
        