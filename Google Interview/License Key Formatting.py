"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
"""
# Solution: Right to Left Traversal

"""
basic idea:
Iterate on the input string in reverse order:
- We will skip '-' characters from the input string.
- If the current character is not '-', we include the current character in ans string and increment the current group size by incrementing count by 1.
- If count reaches k, it means we formed a group of size k, thus we can append a '-' in ans now, and reset count to start counting a new group.
After we finish traversing on the input string, we should check if the last character inserted wasn't a dash. If we find a dash we need to remove it from ans string.

"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        n = len(s)
        answer = []

        for i in reversed(range(n)):
            if (s[i] != "-"):
                answer += s[i].upper()
                count += 1 
                if (count ==k):
                    count = 0
                    answer += "-"
        if (len(answer) > 0 and answer[len(answer) -1] == "-"):
            answer = answer[:-1]
        answer = answer[::-1]
        r = "".join(answer)

        return r
