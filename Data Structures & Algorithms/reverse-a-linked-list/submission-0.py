# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #
        # 3 -> 2 -> 1 -> 0   ===>    3 <- 2 <- 1 <- 0
        #
        return self.reverseList_r(head, None)

    def reverseList_r(self, head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return prev

        new_head = self.reverseList_r(head.next, head)
        head.next = prev
        return new_head