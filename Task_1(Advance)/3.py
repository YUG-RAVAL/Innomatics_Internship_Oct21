class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        a = []
        for i in range(0,len(candies)):
            if (candies[i]+extraCandies >= m):
                a.append(True)
            else:
                a.append(False)
        return a