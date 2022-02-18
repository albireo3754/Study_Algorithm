class Solution:
    def __init__(self):
        self.answer = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        self.answer.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.answer