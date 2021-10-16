class Solution(object):
    def numberOfSteps(self, num):
        c=0
        if num==0:
            return 0
        while(num>0):
            if num%2==0:
                #print(num)
                num=num/2
                c+=1
            else:
                #print(num)
                num=(num-1)/2
                c+=2
        return c-1