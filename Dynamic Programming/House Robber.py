# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         maxMoney = [None for _ in range(len(nums) + 1)]
#         N = len(nums)

#         maxMoney[N], maxMoney[N-1] = 0, nums[N-1]

#         for i in range(N-2,-1,-1):
#             maxMoney[i] = max(maxMoney[i+1], maxMoney[i+2] + nums[i])

#         return maxMoney[0]

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next