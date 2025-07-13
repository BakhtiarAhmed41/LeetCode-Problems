class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head

        seen = set()
        seen.add(head.val)

        prev = head
        current = head.next

        while current:
            if current.val in seen:
                prev.next = current.next
                current = current.next
            else:
                seen.add(current.val)
                prev = current
                current = current.next

        return head
