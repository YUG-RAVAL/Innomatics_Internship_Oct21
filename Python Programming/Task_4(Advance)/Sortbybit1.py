class Solution(object):
    def sortByBits(self, arr):
        res = dict(list)
        for i in arr:
            number = bin(i).count('1')
            res[number].append(i)
        return [i for k in sorted(res) for i in sorted(res[k])]
        
        
        