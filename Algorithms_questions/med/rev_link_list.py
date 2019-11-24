class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        if not head:
            return
        prev = None
        while head:
            tmp = head.next
            head.next=prev
            prev=head
            head = tmp
    # Implement this.

    # Recursive Solution
    def reverseRecursively(self, head):
        if not head:
            return None
        if not head.next:
            return head
        rev_list = self.reverseRecursively(head.next)
        rev_list.next=head
        return head




# Implement this.

# Test Program
# Initialize the test list:
if __name__ == "__main__":
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail

    print("Initial list: ")
    testHead.printList()
    # 4 3 2 1 0
    #testHead.reverseIteratively(testHead)
    testHead.reverseRecursively(testHead)
    print("List after reversal: ")
    testTail.printList()