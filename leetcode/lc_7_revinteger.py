'''
Created on Apr 22, 2016

@author: ewagyae
'''
class Solution(object):
    
    ## Not consider about the number 10, 100, etc. and overflow.
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xstr = str(x)
        xrev = ''
        flag = ''
        if x < 0:
            flag = '-'
            xstr = xstr[1::] 
        for i in xstr:
            xrev = i + xrev
        xrev = flag + xrev
        return int(xrev)
    
    def reverseOpt(self, x):
        rev = ''
        flag = (x < 0 and '-' or '')
        xabs = abs(x)
        while xabs >= 10:
            rem = xabs%10
            xabs = xabs/10
            if rem == 0 and rev == '':
                continue
            rev = rev + str(rem)
        result = int(flag+rev+str(xabs))
        return (result<=2**31-1 and result>=-2**31) and result or 0
            
                

if __name__ == '__main__':
    s = Solution()
    print s.reverseOpt(-100000)