class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if(root):
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        return 0
