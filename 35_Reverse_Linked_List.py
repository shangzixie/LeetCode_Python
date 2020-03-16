

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        self.tail = head
        self.helper(head.next, head)
        return self.head1

    def helper(self, node, prev):
        if not node:
            self.head1 = prev
            return

        self.helper(node.next, node)

        node.next = prev
        prev.next = None

        if node == self.tail:
            node.next = None

class Solution1:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head or not head.next:
            return head
        tail = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return tail



if __name__ == '__main__':
    tail = ListNode(0)
    head = tail
    tail.next = ListNode(1)
    tail = tail.next
    tail.next = ListNode(2)
    tail = tail.next
    tail.next = ListNode(3)
    tail = tail.next

    solution = Solution1()
    solution.reverse(head)