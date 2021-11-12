class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        c = 0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                c+=1
        return c