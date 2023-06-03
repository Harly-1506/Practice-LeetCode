"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
# this problems follow-up of Two Sum

#Solution 01: Two pointers

"""
We'll follow the same two pointers pattern as in Two Sum II. It requires the array to be sorted, so we'll do that first. 
To make sure the result contains unique triplets, We need to skip duplicate values. It is easy to do because repeating values 
are next to each other in a sorted array.

After sorted array, we move our pivot element "num[i]" and analyze them to its right. we find all pairs whose sum is equal "-num[i]"
using two pointer pattern, so that the sum of the pivot element (num[i]) and pair (num[i]) is equal to zero.

As a quick refresher, the pointers are initially set to the first and the last element respectively.
 We compare the sum of these two elements to the target. 
If it is smaller, we increment the lower pointer lo. Otherwise, we decrement the higher pointer hi.
Thus, the sum always moves toward the target, and we "prune" pairs that would move it further away
 Again, this works only if the array is sorted. Head to the Two Sum II solution for the detailed explanation.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i , res)
        return res

    def twoSumII(self, nums, i, res ):
        #set the low pointer lo to i+i and hight pointer hi to the last index
        lo = i+1
        hi = len(nums) - 1

        # same Twosum solution
        while (lo<hi):
            sum = nums[lo] + nums[hi] + nums[i]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                #avoid duplication
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


# Solution 02: Hashset
"""
Since triplets must sum up to the target value, we can try the hash table approach from the Two Sum solution. 
This approach won't work, however, if the sum is not necessarily equal to the target, like in 3Sum Smaller and 3Sum Closest.

We move our pivot element nums[i] and analyze elements to its right. We find all pairs whose sum is equal -nums[i] using the Two Sum: 
One-pass Hash Table approach, so that the sum of the pivot element (nums[i]) and the pair (-nums[i]) is equal to zero.

To do that, we process each element nums[j] to the right of the pivot, and check whether a complement -nums[i] - nums[j] is already in the hashset.
If it is, we found a triplet. Then, we add nums[j] to the hashset, so it can be used as a complement from that point on.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

#Solution 03: No sort
"""
What if you cannot modify the input array, and you want to avoid copying it due to memory constraints?

We can adapt the hashset approach above to work for an unsorted array. We can put a combination of three values into a hashset to 
avoid duplicates. Values in a combination should be ordered (e.g. ascending). Otherwise, we can have results with the same values in the different positions.
"""

"""
The algorithm is similar to the hashset approach above. We just need to add few optimizations so that it works efficiently for repeated values:

1. Use another hashset dups to skip duplicates in the outer loop
 - Without this optimization, the submission will time out for the test case with 3,000 zeroes. This case is handled naturally when the array is sorted.

2. Instead of re-populating a hashset every time in the inner loop, we can use a hashmap and populate it once. Values in the hashmap will indicate whether 
we have encountered that element in the current iteration. When we process nums[j] in the inner loop, 
we set its hashmap value to i. This indicates that we can now use nums[j] as a complement for nums[i].
 - This is more like a trick to compensate for container overheads. The effect varies by language, e.g. 
 for C++ it cuts the runtime in half. Without this trick the submission may time out.

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res