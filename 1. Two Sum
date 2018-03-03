'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
#找出一组数组中两个数之和等于target，并返回这两个数的下标，并且两个数不能重复
#运用两次循环
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        index = []
        for x in range(0,length):
            for y in range(x,length):
                if nums[x]+nums[y] == target and x != y:
                    index.append(x)
                    index.append(y)
                    return index
