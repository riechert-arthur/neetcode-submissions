# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        position = 0
        def recurse(curr: Optional[ListNode], prev: Optional[ListNode]):

            nonlocal position

            if not curr:
                return head

            res = recurse(curr.next, curr)
            position += 1

            if position == n:
                if curr == head: res = curr.next
                if prev: prev.next = curr.next
                
            return res

        return recurse(head, None)