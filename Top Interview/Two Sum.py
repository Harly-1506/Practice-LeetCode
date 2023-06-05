class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                num = nums[i]+(nums[j])
                if num == target:
                    output.append(i)
                    output.append(j)
                
        return output
                