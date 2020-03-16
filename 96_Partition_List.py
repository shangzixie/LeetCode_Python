
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    简单粗暴方法： 两个list 然后合并
    """

    def partition(self, head, x):

        dummy = ListNode("-inf")
        dummy.next = head
        slow = dummy
        fast = dummy

        while fast and fast.next:

            if fast.next.val >= x:
                fast = fast.next
            else:
                if fast == slow:
                    fast = fast.next
                    slow = slow.next
                else:
                    temp = fast.next
                    fast.next = temp.next
                    temp.next = slow.next
                    slow.next = temp
                    slow = temp

        return dummy.next