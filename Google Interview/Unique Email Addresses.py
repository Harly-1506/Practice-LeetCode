"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

"""
#Solution 01: Linear Iteration
"""
1. For each email presnet in the "email" array:
    - Iterate over the characters in the email and append each character to the local name if it is not '.'.
    - If the charactor is '+', do not append the character and break out of the loop
2. Find the domain name using reverse traversal in the given email and append it to string formed till now.
    - After cleaning the email insert it into the hash set
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #hash set to store all the unique emails
        uniqueEmails = set()

        #for loop each email
        for email in emails:
            cleanMail = []

            #for loop each charactor in email
            for currChar in email:
                if currChar == '+' or currChar == '@':
                    break
                if currChar != '.':
                    cleanMail.append(currChar) # email the same without dot

            domainName = []
            for currChar in reversed(email):
                domainName.append(currChar)
                if currChar == "@":
                    break
                
            # local+domain reverse
            domainName = ''.join(domainName[::-1])
            cleanMail = ''.join(cleanMail)
            uniqueEmails.add(cleanMail + domainName)
            
        return len(uniqueEmails)
    

#Solution 02: Using String split method
"""
basic idea:
1. For each email present in the emails array:
    - Split the string into two parts separated by'@', local name, and domain name.
    - Split the local name into parts separated by '+'. Since we do not need the part after '+', let the first part be the local name.
    - Remove all '.' from the local name and append the domain name to it.
    - After cleaning the email, insert it into the hash set.
2. Return the size of the hash set.
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Hash set to store all the unique emails.
        uniqueEmails = set()

        for email in emails:
            # Split into two parts: local and domain.
            name, domain = email.split('@')

             # Split local by '+' and replace all '.' with ''.
            local = name.split('+')[0].replace('.', '')

            # Concatenate local, '@', and domain.
            uniqueEmails.add(local + '@' + domain)

        return len(uniqueEmails)