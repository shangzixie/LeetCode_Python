"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution1:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.

    """

    def sortList(self, head):
        if not head:
            return None

        self.divided(head)
        return head
    '''
    this should  return self.divided(head) not return head
    because 1--> -1 --> null
    head is 1  when return head: 1---null
    '''

    def findMid(self, head):
        slow = head
        fast = head.next

        while fast != None and fast.next != None:  # and
            slow = slow.next
            fast = fast.next.next

        return slow

    def divided(self, node):
        if not node.next or not node:
            return node

        mid = self.findMid(node)
        rightStart = mid.next
        mid.next = None

        left = self.divided(node)
        right = self.divided(rightStart)

        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy = ListNode(None)
        tail = dummy
        p1 = list1
        p2 = list2

        while p1 != None and p2 != None:

            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next

            else:
                tail.next = p2
                p2 = p2.next

            tail = tail.next

        if p1 != None:
            tail.next = p1
        else:
            tail.next = p2

        return dummy.next


class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.

    """

    def sortList(self, head):
        if not head:
            return None


        return self.divided(head)

    def findMid(self, head):
        slow = head
        fast = head.next

        while fast != None and fast.next != None:  # and
            slow = slow.next
            fast = fast.next.next

        return slow

    def divided(self, node):
        if not node.next or not node:
            return node

        mid = self.findMid(node)
        rightStart = mid.next
        mid.next = None

        left = self.divided(node)
        right = self.divided(rightStart)

        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy = ListNode(None)
        tail = dummy
        p1 = list1
        p2 = list2

        while p1 != None and p2 != None:

            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next

            else:
                tail.next = p2
                p2 = p2.next

            tail = tail.next

        if p1 != None:
            tail.next = p1
        else:
            tail.next = p2

        return dummy.next