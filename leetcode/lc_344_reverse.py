'''
Created on Apr 22, 2016

@author: ewagyae
'''
#Write a function that takes a string as input and returns the string reversed.
#
#Example:
#Given s = "hello", return "olleh".


class Solution(object):
    
    def reverseString(self, s):
        newstr = ""
        for i in s:
            newstr = i+newstr
        return newstr
    
    def reverseStringOpt(self, s):
        return s[::-1]
    
if __name__=='__main__':
    s = Solution()
    print s.reverseStringOpt("hello")
        