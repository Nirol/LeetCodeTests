


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        lvl_start=root
        while lvl_start is not None:
            curr_node=lvl_start
            while curr_node is not None:
                if curr_node.left is not None:
                    curr_node.left.next = curr_node.right
                if curr_node.right is not None and curr_node.next is not None:
                    curr_node.right.next=curr_node.next.left
                curr_node=curr_node.next
            lvl_start=lvl_start.left







