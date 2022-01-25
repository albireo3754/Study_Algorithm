# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(next = head)
        array = [root]
        node = head
        while node:
            array.append(node)
            node = node.next
        array.append(None)
        array[-(n + 2)].next = array[-n]
        return root.next