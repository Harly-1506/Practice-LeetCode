#solution 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        key = nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] != key:
                nums[k] = nums[i+1]
                k += 1
                key = nums[i+1]
        
        return k

#solution 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1

        for i in range(1, size):
            #found unique element
            if nums[i -1] != nums[i]:
                #updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                insertIndex +=1

        return insertIndex