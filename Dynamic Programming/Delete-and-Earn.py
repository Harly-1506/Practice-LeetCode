class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        """
        nums = [2,2,3,3,3,4]
        - pick any nums[i] and delete all nums = num[i] +- 1
        - create hasp map 
        - Find a maximun, make decisions numbers to take
        - Recurrence relation: for an arbitrary x, maxPoints(x) = max(maxPoints(x-1), maxPoints(x-2) + gain)
        """
        points = defaultdict(int)
        max_number = 0
        # precompute how many point we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        #Declare our array along with base cases
        max_points = [0]* (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num-1], max_points[num-2]+points[num])

        return max_points[max_number]