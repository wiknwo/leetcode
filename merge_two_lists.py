'''Merge two lists

    William Ikenna-Nwosu (wiknwo)

    Merge two sorted linked lists and return it as a sorted 
    list. The list should be made by splicing together the 
    nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode() # Define head of new list
        current = head # Set current pointer to head
        
        # Iterate through lists
        while l1 != None and l2 != None:
            # If l1 < l2 set l3 next node to l1 otherwise set to l2
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
                
        # Add the rest of l1 values to current
        if l1:
            current.next = l1
        # Add the rest of l2 values to current
        else:
            current.next = l2
        return head.next
        