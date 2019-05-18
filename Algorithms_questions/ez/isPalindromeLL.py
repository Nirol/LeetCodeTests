
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

#not going to implement this solution but with changng the original list its possible:

# step1 : counting the total node in linked list. (N)
# step2 : reverse the last half elements.
# step3 : start from middle element, go left and right.

if __name__ == "__main__":
    x = Solution()
    a = ListNode
    b = ListNode
    c = ListNode
    d = ListNode
    a.val=1
    a.next=b
    b.val=2
    b.next=c
    c.val=2
    c.next=d
    d.val=1
    a.val=5
    ans = x.isPalindrome(a)
    print(ans)


