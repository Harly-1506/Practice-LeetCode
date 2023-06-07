"""
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return true if it is a confusing number, or false otherwise.
"""
# hint: Reverse each digit with their corresponding new digit if an invalid digit is found the return -1. 
# After reversing the digits just compare the reversed number with the original number.
# My solution
class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        """
        1111... hoặc 8888 thì sẽ bỏ qua hoặc 619 hoặc 916
        """
        key = {0:0,
               1:1,
               6:9,
               8:8,
               9:6}
        result = True
        true_nums = [0,1,6,8,9]
        rotation_nums = []

        list_of_digits = [int(x) for x in str(n)]
        for digit in list_of_digits:
            if digit in true_nums: 
                nums = key[digit]
                print(nums)
                rotation_nums.append(nums)
            else: 
                result = False

        if len(rotation_nums)>0:

            rotation_nums.reverse()
            print(rotation_nums)
            if len(rotation_nums)==1:
                nums = rotation_nums[0]
            else: nums = (int(''.join(map(str, rotation_nums))))
            print(nums)
            if nums == n:
                result = False

        return result


#better Sulotion:
class Solution:
    def confusingNumber(self, n: int) -> bool:
        # Use 'invertMap' to invert each valid digit.
        invert_map = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        rotated_number = []
        
        # Iterate over each digit of 'n'.
        for ch in str(n):
            if ch not in invert_map:
                return False

            # Append the inverted digit of 'ch' to the end of 'rotated_number'. 
            rotated_number.append(invert_map[ch])
        
        rotated_number = "".join(rotated_number)

        # Check if the reversed 'rotated_number' equals 'n'.
        return int(rotated_number[::-1]) != n
