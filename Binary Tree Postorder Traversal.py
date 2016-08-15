# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result,p,q = [],None,None
        s = []
        
        if not root:
            return []
        else:
            s.append(root)
        
        while s:
            p = s[-1]
            if (p.left==None and p.right==None) or (q!=None and (p.left == q or p.right == q)):
                result.append(p.val)
                s.pop()
                q=p
                
            else:
                if p.right!=None:
                    s.append(p.right)
                if p.left != None:
                    s.append(p.left)
            
        
        return result
            
