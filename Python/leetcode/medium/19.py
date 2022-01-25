# 배열에 포인터를 저장하는 방식으로 문제를 풀었다.
# 하지만 투포인터를 이용해서 n만큼 node를 뒤로 보내고
# 다시 남은 길이를 이용해서 나머지 길이를 빼주는 방식으로 문제를 품

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