
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



#bfs implementation: keeping in a queue current same level nodes and traversing them, inserting the children to the next level queue.
# in order to implement the zigzag we reversing the values lists if the level%2 -- 1.
# why bfs and not recursion ? in this problem we need to know all the values in a certain level on the same time
# to maintain the requested order, so recursion won't fit.
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return
        ans=[root.va]
        curr=[root]

        level=0


        while curr:
            lvl_list = []
            next_lvl_nodes = []
            for next_node in curr:
                if next_node is not None:
                    lvl_list.append(next_node.val)
                    if next_node.right:
                        next_lvl_nodes.append(next_node.right)
                    if next_node.left:
                        next_lvl_nodes.append(next_node.left)

            if level % 2 ==1:
                lvl_list.reverse()
            ans.append(lvl_list)
            curr=next_lvl_nodes
            level=level+1
        return ans










