# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        n=0
        num=0
        temp=head
        while temp!=None:
            temp=temp.next
            n=n+1
        temp=head
        while temp!=None:
            num=num+(temp.val)*2**(n-1)
            n=n-1
            temp=temp.next
        return num      
