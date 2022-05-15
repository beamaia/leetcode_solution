# Using recursion, very slow and uses a lot of memory

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.sum_height(root, self.height(root))
    
    def height(self, root:TreeNode) -> None:
        if not root.left and not root.right:
            return 1
        
        left_height, right_height = 0, 0

        if root.left:
            left_height = self.height(root.left) + 1
        if root.right:
            right_height = self.height(root.right) + 1
        
        if left_height > right_height:
            return left_height

        return right_height 
    
    def sum_height(self, root: TreeNode, max_height:int):
        height = self.height(root)
                    
        if height == 1 and max_height == height:
            return root.val
        
        left_sum, right_sum = 0, 0
        
        if root.left:
            left_sum = self.sum_height(root.left, max_height - 1)
        if root.right:
            right_sum = self.sum_height(root.right, max_height - 1)
        
        return left_sum + right_sum
    