# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head:
            return None

        # Store the new recursive value
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        # End by ensuring the old listnote head does not link to anything
        head.next = None

        return newHead