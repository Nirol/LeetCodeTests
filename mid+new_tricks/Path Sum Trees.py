
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#the key here is to create outer and inner recursion each outer recurssion for a node will be a "new entry point" to start
# taking nodes val into account in the sum -- that way we can calculate the given task of sums starting for different nodes in the tree
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.num_paths=0
        if root is None:
            return self.num_paths
        return self.num_paths

    def pathSum_recur_outer(self,root,sum):
        if root is None:
            return

        Solution.pathSum_recur_innet(self,root,sum)
        Solution.pathSum_recur_outer(self,root.right,sum)
        Solution.pathSum_recur_outer(self, root.left, sum)

    def pathSum_recur_inner(self,root,sum):
        if root.val == sum:
            self.num_paths+=1
        if root.left is not None:
            Solution.pathSum_recur_inner(self,root.left,sum-root.val)
        if root.right is not None:
            Solution.pathSum_recur_inner(self,root.right,sum-root.val)





