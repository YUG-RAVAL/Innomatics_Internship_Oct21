class Solution(object):
    def numTeams(self, rating):
        n = len(rating)
        increasing = [0]*n
        decreasing = [0]*n
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                if rating[i] < rating[j]:
                    increasing[j] = increasing[j] + 1
                    res = res + increasing[i]
                else:
                    decreasing[j] = decreasing[j] + 1
                    res = res + decreasing[i]
        return res