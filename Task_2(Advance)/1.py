class Solution(object):
    def defangIPaddr(self, address):
        address = list(address)
        for i in range(0,len(address)):
            if address[i] == '.':
                address[i] = '[.]'
        straddress = ''.join(map(str, address))
        return straddress