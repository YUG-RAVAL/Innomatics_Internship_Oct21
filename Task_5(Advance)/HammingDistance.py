class Solution(object):
    def hammingDistance(self, x, y):
        return 0 if not (x or y) else self.hammingDistance(x//2, y//2) + (x%2 != y%2)