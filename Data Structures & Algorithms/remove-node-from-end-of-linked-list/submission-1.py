# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        left= dummy
        right=head

        while n>0 and right:
            right=right.next
            n-=1

        while right:
            left=left.next
            right=right.next

        left.next=left.next.next
        return dummy.next

        




            # 1 2 3 4 n=2
            # 1 2 4

            # 0 1 2 3 4
            # l0 r1 2 3 4 n=2
            # l0 1 r2 3 4 n=1
            # l0 1 2 r3 4 n=0

            # 0 l1 2 3 r4
            # 0 1 l2 3 4 rnone

            # 0 1 2 4
