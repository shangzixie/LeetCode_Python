"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution1:
    """
    version1:
    """

    def reorderList(self, head):
        head2 = self.findMiddle(head)
        head2 = self.reverse(head2)

        return self.merge(head, head2)

    def reverse(self, head):

        prev = ListNode(None)
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev

    def merge(self, head1, head2):
        dummy = ListNode(None)
        dummy.next = head1

        while head1 and head2:
            l1 = head1.next
            head1.next = head2

            l2 = head2.next
            head2.next = l1

            head1 = l1
            head2 = l2
        return dummy.next

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast.next and fast:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        return head2
    """
    edge case: 
    1. None 
    2. just one node: 1-->None 
    """


class Solution:
    """
    so sophisticated
    """

    def reorderList(self, head):
        if not head:
            return head

        head2 = self.findMiddle(head)
        head2 = self.reverse(head2)

        return self.merge(head, head2)

    def reverse(self, head):
        if not head:
            return head

        prev = None  # cannot use ListNode(None)
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev

    def merge(self, head1, head2):
        if not head2:
            return head1

        dummy = ListNode(None)
        dummy.next = head1

        while head1 and head2:
            l1 = head1.next
            head1.next = head2

            l2 = head2.next
            head2.next = l1

            head1 = l1
            head2 = l2
        return dummy.next

    def findMiddle(self, head):
        if not head.next:
            return head

        slow = head
        if head.next:
            fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        return head2






