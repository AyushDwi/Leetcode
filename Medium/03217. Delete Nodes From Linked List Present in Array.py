# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Convert array to set for O(1) lookup
        values_to_remove = set(nums)
        
        # Create dummy node to handle head deletion easily
        dummy = ListNode(0, head)
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val in values_to_remove:
                # Skip the next node (delete it)
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next
        
        return dummy.next
