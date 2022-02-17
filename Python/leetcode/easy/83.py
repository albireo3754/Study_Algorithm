class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current != None and current.next != None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head