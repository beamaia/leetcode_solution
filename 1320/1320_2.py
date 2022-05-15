# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        next_level = []

        while len(queue):
            sum_val = 0
            for node in queue:
                sum_val += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            queue = next_level
            next_level = []

        return sum_val

        
if __name__ == '__main__':
    '''
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # root.right.right.right = TreeNode(8)

    sol = Solution()
    val = sol.deepestLeavesSum(root)
    print(val)