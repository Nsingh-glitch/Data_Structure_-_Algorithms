# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st=[]
        self.func(root)

    def next(self) -> int:
        tmp=self.st.pop()
        self.func(tmp.right)
        return tmp.val
        

    def hasNext(self) -> bool:
        return len(self.st)!=0

    def func(self,node):
        while node:
            self.st.append(node)
            node=node.left




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()