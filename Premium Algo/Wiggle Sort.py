
"""
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

 """

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        My Solutions
        num[0] <= num[1] >= num[2] <= num[3] >= num[4] <= num[5]
        num[1] bigger
        try to slove this in one for loop --> Time complexity is O(n)
        if nums[0] > nums[1] i % 2 == 0:
            swap
        
        [3,5,2,1,6,4]
        [1,2,3,4,5,6]
        output = [1,6,2,5,3,4]
        """

        for i in range(len(nums)-1):

            if nums[i] > nums[i+1] and i % 2 ==0:
                #swap
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
            elif nums[i] < nums[i + 1] and i % 2 !=0:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

