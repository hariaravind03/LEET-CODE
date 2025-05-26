# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,left,right):
        current=left
        prev=None
        end=right.next
        while current!=end:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
        return prev
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy=ListNode(0)
        dummy.next=head
        
        prev=dummy

        for i in range(left-1):
            prev=prev.next
        
        start=prev.next


        end=start

        for i in range(right-left):
            end=end.next

        after=end.next
        reversedhead=self.reverse(start,end)

        prev.next=reversedhead

        start.next=after
        return dummy.next
        
    