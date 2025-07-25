# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tailA=headA
        tailB=headB
        n1=0
        n2=0
        while tailA.next!=None:
            tailA=tailA.next
            n1=n1+1
        while tailB.next!=None:
            tailB=tailB.next
            n2=n2+1
        if tailA!=tailB:
                 return None
        tempA=headA
        tempB=headB
        while n1>n2:
            tempA=tempA.next
            n1=n1-1
        while n1<n2:
            tempB=tempB.next
            n2=n2-1
        while tempA!=None :   
            if tempA==tempB:
                return tempA
            tempA=tempA.next
            tempB=tempB.next
                



        
