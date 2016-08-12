# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result,s = [],[]
       
        if not root:
            return []
        ptr = root
       
        
        while s or ptr:
            if ptr:
                s.append(ptr)
                ptr = ptr.left
            else:
                ptr = s[-1]
                s.pop()
                result.append(ptr.val)
                ptr = ptr.right
                
                
        return result
                
        
