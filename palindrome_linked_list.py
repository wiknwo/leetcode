# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
		"""
		Return boolean indicating if linked list is a palindrome
		
		Time Complexity: O(n)
		Space Complexity: O(n)
		"""
        current, stack = head, []
        # Add all values to the stack
        while current:
            stack.append(current.val)
            current = current.next
        # Reset current
        current = head
        # Iterate through linked list again and
        # pop values from the stack. If the value
        # popped equals the current value then we
        # have palindrome
        while current:
            value = stack.pop()
            if value != current.val:
                return False
            current = current.next
        return True
        
            