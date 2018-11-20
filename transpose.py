# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = []
        seq2 = []
        Solution.rec_leafs(root1, seq1)
        Solution.rec_leafs(root2, seq2)
        ans = cmp(seq1,seq2)
        if ans == 0:
            return True
        else:
            return False

    def rec_leafs(self, root, seq):
        if root.left == None and root.right == None:
            seq.append(root.val)
        if root.left != None:
            Solution.rec_leafs(root.left, seq)
        if root.right != None:
            Solution.rec_leafs(root.right, seq)

if(__name__ == "__main__"):
    x = Solution()
    ans = x.reorderedPowerOf2(456)
    print(ans)