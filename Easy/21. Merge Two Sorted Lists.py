# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1  

        # Ensure list1 starts with the smaller value
        if list2.val < list1.val:
            list1, list2 = list2, list1    

        dummy = ListNode(-1)
        dummy.next = list1
        prev1 = dummy
        curr1 = list1
        Next1 = curr1.next
        curr2 = list2
        Next2 = curr2.next

        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                prev1 = curr1
                curr1 = Next1
                if Next1 is not None:
                    Next1 = Next1.next
                if curr1 is None:
                    prev1.next = curr2
                    return dummy.next
            else:
                prev1.next = curr2
                curr2.next = curr1
                prev1 = curr2
                curr2 = Next2
                if Next2 is not None:
                    Next2 = Next2.next  

        return dummy.next
