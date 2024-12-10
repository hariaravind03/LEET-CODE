class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l= []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        return l