"""
A simple Python program to introduce a linked list 
"""
class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,):
        self.head =  None


#call function
Llist = LinkedList() #init
Llist.head = ListNode(1)
second = ListNode(2)
third = ListNode(3)

#link all node
Llist.head.next = second
second.next = third
#last node is null


"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Solution 01: Recursion

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    
# Solution 02: 
"""
First, we set up a false "prehead" node that allows us to easily return the
head of the merged list later. We also maintain a prev pointer, which
points to the current node for which we are considering adjusting its next
pointer. Then, we do the following until at least one of l1 and l2 points
to null: if the value at l1 is less than or equal to the value at l2,
then we connect l1 to the previous node and increment l1. Otherwise, we
do the same, but for l2. Then, regardless of which list we connected, we
increment prev to keep it one step behind one of our list heads.

After the loop terminates, at most one of l1 and l2 is non-null.
Therefore (because the input lists were in sorted order), if either list is
non-null, it contains only elements greater than all of the
previously-merged elements. This means that we can simply connect the
non-null list to the merged list and return it.
"""
class Solution:
    def mergeTwoLists(self, l1, l2):
        #maintain an unchanging reference to node ahead of the return node
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next