class Solution(object):
    def subtractProductAndSum(self, n):
        p = 1
        s = 0
        st = str(n)
        
        for i in st:
            p = p*int(i)
        for i in st:
            s = s+int(i)
        return (p-s)