'''
Created on Apr 22, 2016

@author: ewagyae
'''
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
#You may assume that each input would have exactly one solution.
#
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#UPDATE (2016/2/13):
#The return format had been changed to zero-based indices. Please read the above updated description carefully.

class Solution(object):
                    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
    
    def twoSumOpt(self, nums, target):
        processed = {}
        for i in range(0, len(nums)):
            if target-nums[i] in processed:
                return [processed[target-nums[i]],i]
            processed[nums[i]]=i
        
            
if __name__ == '__main__':
    s = Solution()
    print s.twoSumOpt([1,2,4,6], 7)