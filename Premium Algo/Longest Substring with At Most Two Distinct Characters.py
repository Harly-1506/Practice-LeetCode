"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.
 """
 # Given List
Alist = ['Mon','Tue','Mon']
print("The given list : ",Alist)

print(len(set(Alist)))
# Compare length for unique elements
if(len(set(Alist)) == len(Alist)):

   print("All elements are unique.")
else:
   print("All elements are not unique.")