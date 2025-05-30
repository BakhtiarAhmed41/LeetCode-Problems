# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        nodes = []

        while list1:
            nodes.append(list1.val)
            list1 = list1.next

        while list2:
            nodes.append(list2.val)
            list2 = list2.next

        if not nodes:
            return None

        nodes.sort()

        head = ListNode(nodes[0])
        current = head
        for val in nodes[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

                

        
