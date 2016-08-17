# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        result = deque()
        current = deque([root])
        
        while current:
            level = []
          #  length = len(current)
            for i in range(len(current)):
                p = current.popleft()
                level.append(p.val)
                if p.left:
                    current.append(p.left)
                if p.right:
                    current.append(p.right)
            
            result.appendleft(level)
        
        return list(result)
                
