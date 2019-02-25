
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        return Solution.rec_reverse_list(self, head, None)

    def rec_reverse_list(self, head, ans):
        if head.next is None:
            head.next = ans
            return head
        else:
            tmp = head.next
            head.next = ans
            return Solution.rec_reverse_list(self, tmp, head)


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5
    x = Solution()
    rev_a1=x.reverse_list(a1)
    print (rev_a1.val)
