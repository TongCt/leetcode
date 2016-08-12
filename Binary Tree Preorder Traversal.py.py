Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result,s = [],[]
        if not root:
            return []
        ptr = root
        s.append(ptr)
        
        while s:
            ptr = s[-1]
            s.pop()
            result.append(ptr.val)
            if ptr.right:
                s.append(ptr.right)
            if ptr.left:
                s.append(ptr.left)
        
        
        return result
        
