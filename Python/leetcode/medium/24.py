# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(next=head)
        node = root
        while node.next and node.next.next:
            next = node.next
            node.next = next.next
            next.next = node.next.next
            node.next.next = next
            node = node.next.next
        return root.next