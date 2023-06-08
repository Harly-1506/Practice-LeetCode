"""Given a string s and an integer k, return the length of the longest 
substring
 of s that contains at most k distinct characters."""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
         
        # My solutions: Easy understand
        #Time complexity O(n) where n is a number of characters 
        """
        base on two distinct
        """
        if len(s) < k:
            return len(s)
        if k == 0:
            return k

        max_len = k
        current_substring = []

        for i in range(len(s)):
            current_substring.append(s[i])
            #check unique characters == 2
            if  len(set(current_substring)) <= k:
                if len(current_substring)> max_len:
                    max_len = len(current_substring)
                # print(current_substring)
            #remove fisrt characters
            while len(set(current_substring)) > k:
                current_substring.pop(0)
        
        return max_len
    
#Sliding window
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        max_size = 0
        counter = collections.Counter()
        
        left = 0
        for right in range(n):
            counter[s[right]] += 1
            
            while len(counter) > k: 
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            max_size = max(max_size, right - left + 1)
                    
        return max_size
    

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_size = 0
        counter = collections.Counter()
        
        for right in range(len(s)):
            counter[s[right]] += 1
            
            if len(counter) <= k:
                max_size += 1
            else:
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]

        return max_size