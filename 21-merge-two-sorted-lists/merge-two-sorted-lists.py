# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        tmp1,tmp2,tmp3=list1,list2,head
        while(tmp1 is not None and tmp2 is not None):
            if(tmp1.val<=tmp2.val):
                tmp3.next=tmp1
                tmp1=tmp1.next
            else:
                tmp3.next=tmp2
                tmp2=tmp2.next
            tmp3=tmp3.next

        if(tmp1 is not None):
            tmp3.next=tmp1
        if(tmp2 is not None):
            tmp3.next=tmp2
        head=head.next
        return head 
        