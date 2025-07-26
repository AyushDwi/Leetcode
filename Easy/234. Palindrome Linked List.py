# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #first of all, I found the middle element
        count=0
        if head==None or head.next==None:
            return True
        temp=head
        while temp!=None:
            temp=temp.next
            count+=1
        temp_count=count   
        count=count//2
        mid=head
        while count>0:
            mid=mid.next
            count=count-1
        if temp_count%2==1:
            mid=mid.next

        # Then I reversed the linked list from the middle element
        prev=None
        curr=mid
        nexT=curr.next
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=nexT
            if nexT!=None:
               nexT=nexT.next
        mid=prev
        # Then I compared values of both the halves of the linked list

        while mid!=None:
            if head.val!=mid.val:
                return False
            head=head.next
            mid=mid.next
        return True        


        
        
