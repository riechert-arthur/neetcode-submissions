# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def r(head, curr):

            if not curr:
                return head

            head = r(head, curr.next)

            if not head:
                return None

            tmp = None
            if head == curr or head.next == curr:
                curr.next = None
            else:
                tmp = head.next
                head.next = curr
                curr.next = tmp
            return tmp

        head = r(head, head.next)