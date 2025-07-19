# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count=0
        if head==None or head.next==None:
            return head
        temp=head
        while temp!=None:
            temp=temp.next
            count+=1
           
        count=count//2
        while count>0:
            head=head.next
            count=count-1
        return head    
