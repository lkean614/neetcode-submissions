# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return

        frontier = head
        length,fast = 1,1
        while head:
            length+=1
            head = head.next

        head = frontier
        if length-1 == n:
            return head.next

        while head:
            fast+=1
            if fast >= length-n:
                head.next = head.next.next
                return frontier
            if fast == 1:
                continue
            head = head.next

        