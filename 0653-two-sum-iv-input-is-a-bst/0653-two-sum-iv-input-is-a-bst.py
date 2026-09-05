# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BST_iterator:
    #reverse=true==next
    #reverse=false==before

    def __init__(self,root,isreverse):
        self.reverse=isreverse
        self.st=[]
        self.func(root)

    def hasnext(self):
        return len(self.st)!=0

    def next(self):
        if self.reverse:
            tmp=self.st.pop()
            self.func(tmp.right)
            return tmp.val
        else:
            tmp=self.st.pop()
            self.func(tmp.left)
            return tmp.val

    def func(self,node):
        if self.reverse:
            while node:
                self.st.append(node)
                node=node.left
        else:
            while node:
                self.st.append(node)
                node=node.right



class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        i = BST_iterator(root, True)
        j = BST_iterator(root, False)

        left = i.next()
        right = j.next()

        while left < right:
            if left + right == k:
                return True

            if left + right < k:
                if i.hasnext():
                    left = i.next()
                else:
                    break
            else:
                if j.hasnext():
                    right = j.next()
                else:
                    break

        return False

