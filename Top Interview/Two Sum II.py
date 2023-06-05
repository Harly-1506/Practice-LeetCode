"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
# Solution
 
"""
We use two indices, initially pointing to the first and the last element, respectively. 
Compare the sum of these two elements with target. If the sum is equal to target, we found 
the exactly only solution. If it is less than target, we increase the smaller index by one. 
If it is greater than target, we decrease the larger index by one. Move the indices and repeat 
the comparison until the solution is found.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1

        while (first < last):
            sum = numbers[first] + numbers[last]
            if sum == target:
                return [first + 1, last + 1]
            elif sum < target:
                first += 1
            else:
                last -= 1

        return [-1,-1]
