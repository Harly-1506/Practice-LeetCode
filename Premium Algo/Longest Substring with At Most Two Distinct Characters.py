"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.
 """
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
 
        # My solutions: Easy understand
        #Time complexity O(n) where n is a number of characters 
        """
        ex: s = "eceba"
            output = 3 with substring is ece that contains at most two distinct characters.
        how to check distinct characters? --> len(set(substring)) == 2
        max_len = 0
        current substring = [e,c]
        for loop 1: [e,c,e]
        for loop 2: [e,c,e,b] #wrong --> drop e and c
        for loop 3: [e, b] 
        """
        if len(s)<3 :
            return len(s)

        max_len = 2
        current_substring = []

        for i in range(len(s)):
            current_substring.append(s[i])
            #check unique characters == 2
            if  len(set(current_substring)) <= 2:
                if len(current_substring)> max_len:
                    max_len = len(current_substring)
                # print(current_substring)
            #remove fisrt characters
            while len(set(current_substring)) > 2:
                current_substring.pop(0)
        
        return max_len

#hashmap solutions: 
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # when the slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len