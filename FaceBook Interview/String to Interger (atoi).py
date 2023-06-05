"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
Return the integer as the final result.
"""

#Solution 01: Follow the Rules

"""Given the rules outlined by the problem's description, we can iterate over the input string and use the given rules to validate it.

First read through the problem statement very carefully. Let's see what are all the possible characters in the input string:

    Whitespaces (' ')
    Digits ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    A sign ('+' or '-')
    Anything else (alphabetic characters, symbols, special characters, etc.)
And write down all the rules for building the integer for each one these characters which will help us in writing down the conditions while building the algorithm"""

# We have 4 Rulues
"""Whitespaces:
 - If any whitespaces occur at the beginning of the input string, we discard them.
 - However, if whitespace occurs anywhere else in the input, then we stop and discard the rest of the input.
 Digits:
 - Discard any leading zeros.
 - Read in all the digit characters until the first non-digit character or the end of the input occur and append those to the output number.
 - If no digits were found, return 0
 Sign:
 - There could be at most one sign character presented at the beginning, or after skipping some whitespaces from the beginning of the input string. 
Otherwise, a sign anywhere else in the input string is not valid and is considered a non-digit character and we stop building the integer.
 - If a '+' or no sign is present, the final number will be a positive integer. On the other hand, the final number will be negative if '-' 
 is the first non-whitespace character in the string.
 Anything else:
 - If any other character not covered by previously defined rules is spotted, we stop building the output number.
 
32-bit Integer Range:
"""
"""
Algorithm
 Initialize two variables:
 - sign (to store the sign of the final result) as 1.
 - result (to store the 32-bit integer result) as 0.
Skip all leading whitespaces in the input string.
Check if the current character is a '+' or '-' sign:
 - If there is no symbol or the current character is '+', keep sign equal to 1.
 - Otherwise, if the current character is '-', change sign to -1.
Iterate over the characters in the string as long as the current character represents a digit or until we reach the end of the input string.
 - Before appending the currently selected digit, check if the 32-bit signed integer range is violated. If it is violated, then return INT_MAX or INT_MIN as appropriate.
 - Otherwise, if appending the digit does not result in overflow/underflow, append the current digit to the result.
Return the final result with its respective sign, sign * result.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)

        #Discard all spaces from the beginning of the input string
        while index < n and s[index] == " ":
            index += 1
        
        #sign = +1, if it's positive number, otherwise sign = -1
        if index < n and s[index] == "+":
            sign = 1
            index += 1
        elif index < n and s[index] == "-":
            sign = -1
            index += 1
        
        #Traverse next digits of input and stop if it is not a digit.
        #End of string is also non-digit character:
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            #check overflow and underflow conditions:
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX %10)):
                return INT_MAX if sign == 1 else INT_MIN

            #Append current digit to the result
            result =  10*result + digit
            index +=1
        
        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result